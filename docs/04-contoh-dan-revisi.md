# 4. Contoh permintaan dan revisi

[Beranda](../README.md) · [Alur pengerjaan](03-alur-pengerjaan.md) · [Pemecahan masalah](05-troubleshooting.md)

Semua nama dan path di sini adalah contoh. Ganti placeholder dengan data sebenarnya. Jangan memakai nomor sertifikat/TR contoh sebagai data produksi.

## A. Siapkan bahan saja

```text
$kemasan-desain
Analisis referensi produk yang saya lampirkan.
Siapkan logo, ilustrasi, background, dan transkripsi teks secara terpisah.
Belum perlu menyusun file Affinity.
Jika pembagian komponen belum jelas, tanyakan dulu.
Simpan di [FOLDER TUJUAN], tanpa ZIP.
```

## B. Buat inner dan label di Affinity

```text
$kemasan-desain
Produk: [NAMA], isi [JUMLAH DAN SATUAN].
Referensi inner: [PATH/FILE].
Referensi label: [PATH/FILE].
Rangka: [PATH/FILE RANGKA].
Ukuran badan/label: [UKURAN DAN SATUAN YANG TERKONFIRMASI].
Produsen: [PERUSAHAAN YANG DIPILIH].
Nomor TR: [NOMOR YANG BENAR, JIKA RELEVAN].
Kolom produksi: Kode Produksi dan Kedaluwarsa.

Analisis referensi, siapkan semua bahan terpisah, lalu periksa bahan.
Setelah siap, satukan pada dokumen Affinity baru dari rangka tersebut.
Teks informasi harus editable. Pertahankan proporsi logo/gambar/QR.
Simpan master, PDF, preview dan bahan ke [FOLDER]. Jangan membuat ZIP.
```

Jika hanya label yang tersedia/diminta, tulis “label saja”; hasilnya memakai awalan `LABEL`, bukan otomatis `INNER DAN LABEL`.

## C. Minta ulang dari gambar

```text
Ulang dari JPG referensi yang saya berikan.
Jangan hanya menyalin master desain lama.
Analisis dan siapkan bahan terpisah dulu; gunakan aset asli yang benar
bila tersedia. Susun dokumen baru dari rangka [FILE].
Perusahaan yang dipakai: [CV/PT DAN NAMA].
Nomor TR: [NOMOR YANG DIPILIH].
```

Perbedaan utamanya adalah sumber layout dan urutan persiapan. Aset asli yang memang sesuai tidak harus direkonstruksi ulang dengan AI.

## D. Koreksi satu ukuran

```text
Panjang badan dus menjadi 70 mm, sebelumnya 75 mm.
Penampang lainnya tetap. Sesuaikan panel, flap dan garis lipat terkait.
Ukuran label tetap seperti sebelumnya.
Jangan meregangkan tulisan, logo, gambar atau QR.
Pertahankan edit saya pada dokumen aktif.
```

Angka di atas hanya contoh koreksi. Jika “panjang” dapat menunjuk ke beberapa bidang, agent perlu memastikan dimensi yang dimaksud.

## E. Buat varian isi baru

```text
Buat versi [ISI BARU] dari master terbaru yang disetujui.
Ukuran dus dan label [TETAP SAMA / UKURAN BARU].
Komposisi: [DATA VARIAN YANG TELAH DISETUJUI].
Nomor TR: [NOMOR YANG DIGUNAKAN].
Produsen dan format kolom tetap seperti keputusan sebelumnya.
Simpan sebagai varian terpisah; jangan menimpa versi lama.
```

Jika komposisi atau TR belum diketahui, agent menanyakannya dahulu. Jangan mengalikan dosis secara otomatis karena volume botol berubah.

## F. Ganti logo perusahaan

```text
Ganti logo [JENIS] dengan aset [FILE].
Pemilik sertifikat/perusahaan: [NAMA].
Terapkan pada [DOKUMEN/PENEMPATAN YANG DIMINTA].
Pertahankan nomor, proporsi, QR dan isi lain di luar revisi.
Jika hubungan produk dengan pemilik sertifikat belum jelas, tanyakan.
```

Untuk banyak desain, sebutkan “seluruh master pada folder …” dan perusahaan yang dimaksud. Menambah sebuah pustaka logo saja tidak otomatis meminta semua proyek lama diubah.

## G. Ubah format kolom

```text
Gunakan format baru: Kode Produksi dan Kedaluwarsa.
Ganti pada seluruh inner/label yang memiliki kolom tersebut.
Periksa supaya tulisan yang lebih panjang tetap muat.
Perbarui bahan teks, master, PDF dan preview.
```

## H. Scan satu bagian

```text
$kemasan-desain
Transkripsikan hanya bagian komposisi dari gambar ini.
Ikuti ejaan/angka sumber; tandai bagian yang tidak terbaca.
Cukup kirim teks siap salin, tanpa folder atau ZIP baru.
```

Untuk memulai proyek lengkap, salin dan isi [template brief](../examples/brief-produk.md).
