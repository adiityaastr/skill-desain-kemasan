# 2. Instalasi dan koneksi

[Beranda](../README.md) · [Persiapan](01-persiapan.md) · [Alur pengerjaan](03-alur-pengerjaan.md)

Ada dua hal terpisah: memasang **instruksi skill** dan menyediakan **tool kerja**. Clone repositori hanya memasang instruksi/referensi/helper.

## Memasang pada Codex

Dokumentasi Codex saat diperiksa pada 20 November 2026 mencantumkan `~/.agents/skills/` untuk skill pengguna dan `.agents/skills/` dalam proyek. Skill bisa dipanggil dengan `$kemasan-desain`; jika belum terlihat setelah pemasangan, coba mulai ulang Codex. Ikuti [panduan resmi](https://learn.chatgpt.com/docs/build-skills) jika versi aplikasi berbeda.

### Windows dengan Git

Jalankan di PowerShell. Perintah berhenti jika folder tujuan sudah ada, agar pemasangan lama tidak tertimpa.

```powershell
$skillParent = Join-Path $env:USERPROFILE '.agents\skills'
$skillTarget = Join-Path $skillParent 'kemasan-desain'
if (Test-Path -LiteralPath $skillTarget) {
    throw 'Skill sudah ada. Periksa pemasangan lama sebelum memperbarui.'
}
New-Item -ItemType Directory -Path $skillParent -Force | Out-Null
git clone https://github.com/adiityaastr/skill-desain-kemasan.git $skillTarget
```

Untuk macOS/Linux:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/adiityaastr/skill-desain-kemasan.git ~/.agents/skills/kemasan-desain
```

### Tanpa Git

1. Unduh repositori melalui **Code → Download ZIP** di GitHub.
2. Ekstrak, lalu ubah nama folder hasil menjadi `kemasan-desain`.
3. Taruh seluruh folder pada direktori skill yang dibaca agent Anda.
4. Pastikan `kemasan-desain/SKILL.md` langsung tersedia, bukan berada di folder bersarang tambahan.

Mengunduh ZIP untuk instalasi skill berbeda dari membuat ZIP hasil desain. Hasil desain tetap berupa folder kecuali pengguna meminta ZIP.

Sebagian lingkungan lama/kustom masih menggunakan `~/.codex/skills/`. Periksa daftar skill dan path yang dibaca lingkungan Anda. Jangan memasang dua salinan bernama sama tanpa mengetahui mana yang sedang digunakan.

### Uji pemasangan

Kirim ke agent:

```text
Gunakan $kemasan-desain. Sebutkan file SKILL.md yang Anda baca,
lalu jelaskan bahan apa yang perlu saya siapkan untuk membuat label.
Belum perlu membuat atau mengubah desain.
```

Pemasangan terbaca bila agent menemukan skill yang benar dan mengikuti alurnya. Ini belum membuktikan koneksi Affinity atau imagegen tersedia.

## Menyediakan tool Affinity

Server MCP Affinity berjalan lokal. Pada versi yang mendukungnya, konfigurasi MCP berada di Settings aplikasi Affinity; nama menu dapat berbeda menurut versi. Lihat [halaman konektor Affinity buatan Canva](https://claude.com/marketplace/connectors/affinity-106b90) dan [SDK resmi](https://sdk.affinity.studio/).

1. Buka dan masuk ke aplikasi Affinity yang mendukung scripting/MCP.
2. Aktifkan konfigurasi server MCP yang disediakan aplikasi.
3. Hubungkan agent/klien ke server tersebut sesuai petunjuk klien dan informasi yang ditampilkan aplikasi.
4. Biarkan aplikasi berjalan selama agent mengerjakan dokumen.
5. Pastikan agent melihat tool seperti `read_sdk_documentation_topic`, `execute_script` dan `render_spread` (awalan nama tool bisa berbeda).

Untuk konfigurasi klien Codex, gunakan [panduan MCP resmi](https://learn.chatgpt.com/docs/extend/mcp?surface=cli). Repositori ini tidak membundel server, bridge, URL/port tetap, atau konfigurasi konektor. Transport dan autentikasi mengikuti versi aplikasi/klien; konektor pada satu klien tidak otomatis terpasang di klien lain.

Uji dengan permintaan read-only:

```text
Periksa koneksi Affinity: baca preamble SDK, lalu daftar judul/path
serta status perubahan dokumen yang terbuka. Jangan ubah dokumen.
```

Bila ini berhasil, agent bisa mencoba render dokumen contoh yang Anda pilih. Bila tool tidak tersedia, gunakan skill untuk bahan/teks terlebih dahulu dan lakukan penggabungan manual; jangan mengklaim file Affinity sudah dibuat otomatis.

## Tool gambar

Gunakan tool generasi/edit gambar yang benar-benar tersedia pada agent. Skill tidak memasang imagegen atau mengubah langganan AI menjadi akses API. Jika hanya perlu teks, bentuk native, atau memakai aset asli yang sudah baik, generasi gambar baru tidak selalu diperlukan.

Minta alpha nyata untuk aset transparan. Untuk logo khusus, catat apakah aset asli atau rekonstruksi. Untuk sertifikasi dan QR, sediakan sumber yang tepat; jangan merekonstruksi nomor/kode dengan AI.

## Helper Python opsional

Jalankan dari folder skill:

```bash
python --version
python scripts/layout_geometry.py --help
python scripts/package_assets.py --help
```

Helper geometri dan ZIP memakai pustaka standar Python. Untuk inspeksi gambar, pasang Pillow bila belum tersedia:

```bash
python -m pip install Pillow
python scripts/package_assets.py inspect path/to/image.png
```

Perintah inspeksi membaca metadata dan alpha; bukan penghapus background atau penajam gambar. Helper geometri menghitung ukuran ideal; bukan alat untuk memastikan botol nyata cocok atau desain siap cetak. ZIP hanya bila diminta:

```bash
python scripts/package_assets.py package path/to/staging --output path/to/paket.zip
```

Untuk menguji helper:

```bash
python -m unittest discover -s tests
```

## Memperbarui pemasangan

Jika memasang melalui Git, periksa `git status` pada folder skill terlebih dahulu. Jika bersih dan tidak ada modifikasi lokal yang ingin dipertahankan, gunakan `git pull --ff-only`. Jika ada perubahan lokal, simpan atau tinjau dahulu; jangan menggunakan reset paksa untuk menghapusnya.
