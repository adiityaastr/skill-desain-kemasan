# Skill Desain Kemasan

Skill berbahasa Indonesia untuk menyiapkan bahan, membuat, mengadaptasikan, dan merevisi desain kemasan dari gambar referensi, brief, atau rangka. Mendukung inner/dus, label, pouch, sachet, sleeve, serta penyusunan di Affinity bila tool tersedia.

## Isi

- `SKILL.md`: instruksi utama dan alur kerja.
- `references/`: adaptasi ukuran, pemisahan komponen, logo perusahaan, Affinity, dan penyerahan hasil.
- `scripts/`: perhitungan geometri, inspeksi gambar, dan ZIP jika diminta.
- `tests/`: pemeriksaan helper geometri.
- `agents/openai.yaml`: metadata skill.

## Memasang dan menggunakan

Salin seluruh isi repositori ke folder `kemasan-desain` dalam direktori skill agent Anda. Untuk Codex, lokasi umumnya `~/.codex/skills/kemasan-desain/`. Muat ulang daftar skill bila diperlukan, lalu panggil `$kemasan-desain` bersama referensi, ukuran, atau file rangka.

Contoh permintaan:

```text
Gunakan $kemasan-desain untuk menganalisis gambar produk ini,
menyiapkan bahan terpisah, lalu merakitnya di Affinity memakai rangka yang saya berikan.
```

## Perilaku utama

- Analisis dan pisahkan gambar, teks, serta bentuk sebelum menyusun desain.
- Tanyakan komponen yang ambigu, nomor TR, konflik produsen CV/PT, serta format kolom produksi/kedaluwarsa bila belum ditentukan.
- Cocokkan logo sertifikasi dengan pemilik dan sumber yang sesuai; tidak ada perusahaan bawaan.
- Periksa ukuran fisik tiap bidang, geometri rangka, proporsi gambar/kode dan overflow teks.
- Konfirmasi komposisi dan TR varian baru; simpan setiap varian terpisah.
- Gunakan nama `INNER`, `LABEL`, atau `INNER DAN LABEL` sesuai isi file, diikuti nama produk dan ukuran isi.
- Serahkan folder desain; ZIP dibuat hanya jika diminta.
- Periksa hasil tersimpan, PDF dan preview setelah perubahan terakhir.

Skill tidak menyertakan aset merek, sertifikat, atau QR produk. Tool Affinity dan imagegen perlu tersedia pada agent untuk menjalankan bagian terkait; helper Python tidak memasang integrasi tersebut.

## Helper Python

Python 3 diperlukan untuk helper. Pillow opsional untuk inspeksi gambar.

```bash
python scripts/layout_geometry.py cylinder --diameter 57 --height 51 --overlap 3
python scripts/package_assets.py inspect path/to/image.png
python -m unittest discover -s tests
```

Perhitungan keliling memakai bentuk silinder ideal; ukuran produksi tetap mengikuti rangka dan spesifikasi proyek.
