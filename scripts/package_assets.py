#!/usr/bin/env python3
"""Inspect images read-only, or package staged design assets into a new ZIP."""
import argparse
import hashlib
import json
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

MANIFEST = 'ASSET-MANIFEST.json'
IMAGES = {'.png', '.jpg', '.jpeg', '.webp', '.tif', '.tiff'}
ORIGINS = {'source', 'extracted', 'reconstructed', 'unspecified'}


def inspect_image(path):
    try:
        from PIL import Image
    except ImportError:
        return {'inspection': 'unavailable', 'reason': 'Pillow is not installed'}
    with Image.open(path) as im:
        info = {'width': im.width, 'height': im.height, 'mode': im.mode, 'format': im.format}
        rgba = im.convert('RGBA')
        lo, hi = rgba.getchannel('A').getextrema()
        info['alpha'] = {'min': lo, 'max': hi, 'has_transparency': lo < 255,
                         'corners': [rgba.getpixel(p)[3] for p in
                                     [(0, 0), (im.width-1, 0), (0, im.height-1), (im.width-1, im.height-1)]]}
        x = min(im.width-1, round(im.width * 0.1))
        def yellow(y):
            r, g, b, a = rgba.getpixel((x, y))
            return a >= 200 and r >= 180 and g >= 140 and b <= 110 and r-b >= 80
        y = im.height - 1
        while y >= int(im.height * 0.8) and yellow(y):
            y -= 1
        if y < im.height - 1:
            info['yellow_footer_sample'] = {'x': x, 'y_start': y+1, 'height': im.height-y-1,
                                           'note': 'Heuristic sample; verify visually.'}
        return info


def package(stage, output):
    stage = stage.resolve(strict=True)
    output = output.resolve()
    if not stage.is_dir():
        raise ValueError('Staging must be a directory')
    if stage == output or stage in output.parents:
        raise ValueError('Output ZIP must be outside staging')
    if output.suffix.lower() != '.zip':
        raise ValueError('Output must end in .zip')
    if output.exists():
        raise ValueError('Output exists; use a new versioned filename')
    files = []
    for path in sorted(stage.rglob('*')):
        if path.is_symlink():
            raise ValueError('Symlink in staging: ' + str(path.relative_to(stage)))
        if not path.is_file():
            continue
        name = path.name.lower()
        if (path.name == MANIFEST or name == '.env' or name.startswith('.env.') or
                name in {'id_rsa', 'id_ed25519'} or path.suffix.lower() in {'.pem', '.key', '.pfx', '.p12', '.zip'}):
            raise ValueError('Reserved/key/archive file in staging: ' + str(path.relative_to(stage)))
        files.append((path, path.relative_to(stage).as_posix()))
    if not files:
        raise ValueError('No assets in staging')
    source = stage / 'provenance.json'
    provenance = json.loads(source.read_text(encoding='utf-8-sig')) if source.exists() else {}
    if not isinstance(provenance, dict):
        raise ValueError('Provenance must map relative paths to metadata')
    if set(provenance) - {rel for _, rel in files}:
        raise ValueError('Provenance refers to missing assets')
    manifest = {'created_at': datetime.now(timezone.utc).isoformat(), 'files': [],
                'limitations': 'Metadata is not proof of source fidelity or print readiness.'}
    for path, relative in files:
        metadata = provenance.get(relative, {'origin': 'unspecified'})
        if not isinstance(metadata, dict) or metadata.get('origin', 'unspecified') not in ORIGINS:
            raise ValueError('Invalid provenance for ' + relative)
        digest = hashlib.sha256()
        with path.open('rb') as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b''):
                digest.update(chunk)
        record = {'path': relative, 'bytes': path.stat().st_size,
                  'sha256': digest.hexdigest(), 'provenance': metadata}
        if path.suffix.lower() in IMAGES:
            record['image'] = inspect_image(path)
        manifest['files'].append(record)
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'x', compression=zipfile.ZIP_DEFLATED) as archive:
        for path, relative in files:
            archive.write(path, relative)
        archive.writestr(MANIFEST, json.dumps(manifest, ensure_ascii=False, indent=2))
    with zipfile.ZipFile(output) as archive:
        bad = archive.testzip()
        if bad:
            raise ValueError('ZIP integrity failure: ' + bad)
    return {'zip': str(output), 'asset_count': len(files), 'bytes': output.stat().st_size}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    inspect_cmd = commands.add_parser('inspect', help='Inspect without editing images')
    inspect_cmd.add_argument('images', nargs='+', type=Path)
    pack_cmd = commands.add_parser('package', help='Create ZIP with a hash manifest; never overwrite')
    pack_cmd.add_argument('stage', type=Path)
    pack_cmd.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        result = ([{'file': str(p), **inspect_image(p)} for p in args.images] if args.command == 'inspect'
                  else package(args.stage, args.output))
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print('Error: ' + str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
