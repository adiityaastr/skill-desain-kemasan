# 5. Pemecahan masalah

[Beranda](../README.md) · [Instalasi dan koneksi](02-instalasi-dan-koneksi.md)

| Gejala | Periksa dan lakukan |
| --- | --- |
| `$kemasan-desain` tidak ditemukan | Pastikan seluruh folder terpasang di lokasi yang dibaca agent, `SKILL.md` langsung berada di dalamnya, dan tidak ada folder bersarang ekstra. Muat ulang agent bila perlu. |
| Agent membaca skill versi lama | Minta path skill yang benar-benar dibaca. Periksa salinan ganda dan pembaruan Git, tanpa menghapus edit lokal secara paksa. |
| Skill terbaca tetapi Affinity tidak tersambung | Skill dan MCP terpisah. Periksa aplikasi, server MCP, konfigurasi klien dan daftar tool. Lihat [uji koneksi](02-instalasi-dan-koneksi.md#menyediakan-tool-affinity). |
| Tidak ada tool gambar | Gunakan aset sumber yang tersedia atau sediakan tool yang sesuai. Jangan mengaku gambar sudah digenerate jika tool tidak tersedia. |
| File lokal tidak bisa dibuka | Pastikan agent memiliki akses folder. Pada chat tanpa filesystem lokal, lampirkan file; path komputer saja tidak cukup. |
| SDK menolak path proyek | Ikuti pembatasan filesystem aplikasi. Jika staging diperbolehkan, simpan di lokasi yang diizinkan lalu salin hasil ke proyek dan verifikasi salinan. Jangan mengklaim file tujuan sudah terbuka jika yang terbuka masih staging. |
| Koneksi macet setelah aplikasi dimulai ulang | Periksa status dokumen dengan koneksi baru bila tersedia. Jangan mengulang mutasi yang status akhirnya belum diketahui atau menutup aplikasi yang menyimpan edit pengguna. |
| Generasi AI mengubah logo/nomor | Gunakan sumber asli, atau jelaskan rekonstruksi. Sertifikasi dan QR tidak boleh ditebak. Jika font hanya mirip, sebutkan sebagai pendekatan. |
| Background terlihat putih atau berpola kotak | Periksa alpha sebenarnya, rongga/celah, dan layer belakang. Checkerboard pada preview harus dibedakan dari pola yang tertanam pada gambar. |
| Ukuran halaman benar, artwork salah | Ukur bidang jadi dan panel, bukan hanya artboard. Pisahkan badan dus, flap, bleed dan label. |
| Cetakan lebih kecil/besar | Periksa Actual Size / 100%, unit, ukuran PDF, dan pengaturan printer. Jangan memakai Fit to Page untuk uji ukur. |
| Label tidak menutup keliling botol | Ukur permukaan tempel aktual, gap/overlap serta stiker lama bila ditimpa. Keliling ideal `pi × diameter` belum memperhitungkan bentuk meruncing atau toleransi. |
| Teks meluber setelah “Kode Produksi” | Periksa frame, spacing, leading dan ruang tulis. Sesuaikan layout lalu periksa hasil render; jangan menghapus informasi agar muat. |
| Versi baru masih menyebut isi lama | Periksa seluruh muka, judul komposisi, jumlah bahan, artboard, PDF/preview serta bahan teks. Jangan sekadar mengganti nama file. |
| QR tampak persegi tetapi gagal dibaca | Periksa sumber, resolusi, quiet zone, proporsi dan lapisan yang menutupinya. Uji pembacaan pada render/cetak bila tersedia. |
| ZIP dibuat padahal tidak diminta | Keluaran default adalah folder. Helper `package` memang membuat ZIP dan hanya dijalankan saat kompresi diminta. |

## Cara melaporkan masalah agar mudah diperbaiki

Kirim bagian yang salah, hasil yang diinginkan, file/path relevan, ukuran yang sudah diukur, dan keputusan yang sudah diberikan. Jika bisa, tandai lokasi pada screenshot; jelaskan bahwa tanda koreksi bukan bagian artwork.

```text
Yang salah: [bagian/lokasi].
Yang diinginkan: [perubahan spesifik].
Master yang dipakai: [FILE].
Ukuran terkonfirmasi: [DIMENSI + SATUAN].
Bagian yang tetap dipertahankan: [DAFTAR].
```

Gambar dokumentasi di repo adalah skema edukasi, bukan bukti bahwa integrasi pada komputer Anda telah aktif. Untuk fitur/konfigurasi versi terbaru, gunakan tautan resmi di [panduan instalasi](02-instalasi-dan-koneksi.md).
