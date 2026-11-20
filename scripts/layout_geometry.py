#!/usr/bin/env python3
"""Read-only physical dimensions: proportional fit/cover and cylindrical wrap."""
import argparse
import json
import math
import sys

MM_PER_UNIT = {'mm': 1.0, 'cm': 10.0, 'in': 25.4, 'pt': 25.4 / 72.0}


def number(value, name, allow_zero=False):
    value = float(value)
    if not math.isfinite(value) or value < 0 or (value == 0 and not allow_zero):
        raise ValueError(f'{name} must be finite and ' + ('nonnegative' if allow_zero else 'positive'))
    return value


def to_mm(value, unit='mm', dpi=None):
    value = number(value, 'dimension', allow_zero=True)
    if unit == 'px':
        if dpi is None:
            raise ValueError('Pixel dimensions require an explicit DPI')
        return value * 25.4 / number(dpi, 'DPI')
    if unit not in MM_PER_UNIT:
        raise ValueError('Unsupported unit: ' + str(unit))
    return value * MM_PER_UNIT[unit]


def fit(source_width, source_height, target_width, target_height,
        source_unit='mm', target_unit='mm', source_dpi=None, target_dpi=None):
    sw = to_mm(number(source_width, 'source width'), source_unit, source_dpi)
    sh = to_mm(number(source_height, 'source height'), source_unit, source_dpi)
    tw = to_mm(number(target_width, 'target width'), target_unit, target_dpi)
    th = to_mm(number(target_height, 'target height'), target_unit, target_dpi)
    sx, sy = tw / sw, th / sh
    contain, cover = min(sx, sy), max(sx, sy)
    matches = math.isclose(sw / sh, tw / th, rel_tol=1e-6, abs_tol=1e-12)
    return {
        'source_mm': {'width': sw, 'height': sh},
        'target_mm': {'width': tw, 'height': th},
        'aspect_ratio_matches': matches,
        'layout_choice_needed_if_not_already_decided': not matches,
        'contain': {
            'uniform_scale': contain,
            'artwork_mm': {'width': sw * contain, 'height': sh * contain},
            'total_extra_space_mm': {'horizontal': max(0, tw - sw * contain),
                                     'vertical': max(0, th - sh * contain)},
        },
        'cover': {
            'uniform_scale': cover,
            'artwork_mm': {'width': sw * cover, 'height': sh * cover},
            'total_crop_mm': {'horizontal': max(0, sw * cover - tw),
                              'vertical': max(0, sh * cover - th)},
        },
        'nonuniform_scaling_for_comparison_only': {'x': sx, 'y': sy},
        'note': 'No rotation or editing performed. Different X/Y scales distort content; '
                'choose proportional fit, permitted crop, or reflow. Margins/bleed are not inferred.',
    }


def cylinder(diameter, unit='mm', overlap=None, gap=None, height=None):
    if unit not in MM_PER_UNIT:
        raise ValueError('Cylinder measurements require a physical unit')
    if overlap is not None and gap is not None:
        raise ValueError('Choose gap or overlap, not both')
    diameter_mm = to_mm(number(diameter, 'diameter'), unit)
    circumference = math.pi * diameter_mm
    extra = to_mm(number(overlap, 'overlap', True), unit) if overlap is not None else 0
    missing = to_mm(number(gap, 'gap', True), unit) if gap is not None else 0
    length = circumference + extra - missing
    if length <= 0:
        raise ValueError('Gap must be smaller than the circumference')
    return {
        'diameter_mm': diameter_mm,
        'circumference_mm': circumference,
        'overlap_mm': extra,
        'gap_mm': missing,
        'label_length_mm': length,
        'label_height_mm': to_mm(number(height, 'height'), unit) if height is not None else None,
        'note': 'Ideal cylinder only. Verify the actual application surface and print at 100%. '
                'No taper, manufacturing allowance or overlap default is inferred.',
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    resize = commands.add_parser('fit', help='Compare physical sizes without changing files')
    for prefix in ('source', 'target'):
        resize.add_argument('--' + prefix + '-width', type=float, required=True)
        resize.add_argument('--' + prefix + '-height', type=float, required=True)
        resize.add_argument('--' + prefix + '-unit', choices=(*MM_PER_UNIT, 'px'), default='mm')
        resize.add_argument('--' + prefix + '-dpi', type=float)
    wrap = commands.add_parser('cylinder', help='Calculate a cylindrical label length')
    wrap.add_argument('--diameter', type=float, required=True)
    wrap.add_argument('--height', type=float)
    wrap.add_argument('--unit', choices=tuple(MM_PER_UNIT), default='mm')
    seam = wrap.add_mutually_exclusive_group()
    seam.add_argument('--overlap', type=float)
    seam.add_argument('--gap', type=float)
    args = vars(parser.parse_args(argv))
    command = args.pop('command')
    try:
        result = fit(**args) if command == 'fit' else cylinder(**args)
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    except (ValueError, OverflowError) as error:
        print('Error: ' + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
