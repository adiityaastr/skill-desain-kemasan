# 1. Persiapan sebelum mulai

[Beranda](../README.md) · [Berikutnya: instalasi](02-instalasi-dan-koneksi.md)

Tentukan keluaran terlebih dahulu: transkripsi teks, bahan desain saja, revisi satu aset, atau master Affinity. Kebutuhan file berbeda untuk setiap pekerjaan.

## Perangkat dan tool

| Kebutuhan | Kapan diperlukan | Cara mengecek |
| --- | --- | --- |
| Agent AI yang mendukung skill | Semua alur | Agent dapat menemukan dan membaca `kemasan-desain/SKILL.md`. |
| Pembaca gambar dan akses file | Analisis gambar/aset | Agent bisa membuka referensi dan menyimpan hasil pada folder tujuan. |
| Tool generasi/edit gambar | Membuat atau merekonstruksi bitmap | Agent mengonfirmasi tool tersedia sebelum menjanjikan generate. |
| Affinity dengan integrasi scripting/MCP | Penyusunan otomatis file native | Agent dapat membaca dokumen, menjalankan script, dan merender spread. |
| Python 3 | Helper geometri, inspeksi dan pengemasan opsional | `python --version` berhasil. |
| Pillow | Metadata/alpha gambar lewat helper | `python -c "from PIL import Image; print(Image.__version__)"` berhasil. |
| Git | Instalasi/pembaruan lewat Git | `git --version` berhasil. Download ZIP repositori juga bisa dipakai. |

Membaca instruksi skill tidak membutuhkan API key. Akses model, tool gambar, atau layanan lain mengikuti aplikasi dan penyedia yang Anda pilih; repo ini tidak menyediakan akun, kredensial, atau layanan tersebut. Affinity tidak diperlukan untuk transkripsi satu paragraf atau menyiapkan bahan saja.

## File yang disiapkan

| Bahan | Yang diharapkan |
| --- | --- |
| Referensi desain | JPG/PNG jelas; seluruh sisi yang diminta terlihat. PDF asli lebih berguna jika masih berisi teks/bentuk. |
| Master lama, bila melanjutkan | File native terbaru, termasuk edit yang sedang aktif. Jelaskan file mana yang menjadi dasar. |
| Rangka/dieline | File `.af` atau format yang dapat dibaca tool; sebutkan unit, bidang potong/lipat dan ukuran jadi. |
| Ukuran label | Panjang × tinggi, satuan, serta gap/overlap bila melingkari botol. |
| Data produk | Nama, isi, komposisi, manfaat/petunjuk dan informasi yang memang harus dicantumkan. |
| Produsen/distributor | Nama perusahaan yang dipilih; sebutkan CV/PT jika acuan berbeda. |
| Nomor registrasi/TR | Nomor yang benar untuk produk/varian tersebut, jika relevan. Jangan mengandalkan nomor contoh. |
| Logo/sertifikat/QR | Aset dari pemilik/penerbit yang sesuai, beserta pemetaan produknya jika perlu. |
| Font | File font yang boleh digunakan, atau izin memakai font pendekatan bila asli tidak tersedia. |
| Spesifikasi produksi | Bleed, safe area, profil warna dan ketentuan percetakan bila targetnya produksi. |
| Tujuan penyimpanan | Folder proyek dan keluaran yang diminta: master, bahan, PDF, preview. |

Jangan mengambil ukuran fisik hanya dari DPI gambar atau screenshot. Jika hanya meminta bahan atau konsep, informasi cetak yang belum tersedia dapat dicatat sebagai belum dikonfirmasi.

## Keputusan yang akan ditanyakan

- Yang dibuat inner saja, label saja, atau keduanya?
- Ukuran memakai rangka mana? Apakah ada koreksi ukuran terbaru?
- Teks/gambar apa yang harus terpisah atau editable?
- Nomor TR dan perusahaan mana yang dipakai jika sumber berbeda?
- Format kolom lama `Batch No` / `Exp Date` atau baru `Kode Produksi` / `Kedaluwarsa`, bila kolom itu ada?
- Untuk varian baru, komposisi dan ukuran fisiknya tetap atau berubah?

Jawaban yang sudah diberikan pada rangkaian proyek yang sama tidak perlu diulang. Jika keputusan diperlukan, agent melanjutkan pekerjaan lain yang tidak bergantung padanya sambil menunggu jawaban.

## Contoh folder sumber

```text
SUMBER-PRODUK/
├── referensi-inner.jpg
├── referensi-label.jpg
├── rangka.af
├── teks-produk.txt
├── logo-perusahaan/
└── font/
```

Ini contoh susunan, bukan struktur wajib. Hindari hanya mengirim nama file yang tidak bisa diakses agent. Untuk agent lokal, berikan path lengkap; untuk chat tanpa akses filesystem, lampirkan file yang diperlukan.

Isi [template brief](../examples/brief-produk.md), lalu lanjut ke [instalasi dan koneksi](02-instalasi-dan-koneksi.md).
