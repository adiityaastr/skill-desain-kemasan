# Adaptasi jenis, ukuran dan bentuk kemasan

Baca untuk membuat/adaptasi layout fisik. Gunakan bidang yang tersedia dan batas produksi, bukan ukuran satu produk contoh.

## Ukuran dan satuan

- Ambil ukuran dari instruksi, rangka/native/PDF terukur, spesifikasi percetakan dan pengukuran fisik yang relevan. Jika bertentangan, pastikan keputusan sebelum mengubah geometri.
- Pisahkan **halaman**, **artwork**, **ukuran jadi/trim**, **bleed**, **safe area**, **area segel/sambungan**, dan **potong/lipat**. Margin putih PDF bukan otomatis bagian label. Flap dan tab lem bukan bidang badan dus.
- Bitmap hanya memberi piksel. DPI metadata dapat membantu konversi, tetapi tidak membuktikan ukuran cetak yang dimaksud. Jangan memakai DPI layar sebagai DPI sumber/cetak. Jika ukuran belum ada, minta hanya ukuran yang diperlukan atau tandai sebagai konsep.
- Konversi eksplisit: 1 cm = 10 mm; 1 in = 25,4 mm; 1 pt = 25,4/72 mm. Piksel ke mm memerlukan DPI yang diketahui.
- Bleed, safe area, quiet zone kode, toleransi potong, resolusi efektif dan profil warna mengikuti spesifikasi proyek/media. Jangan menetapkan 3 mm atau 300 DPI sebagai angka universal. Rekomendasi yang belum dikonfirmasi harus disebut asumsi.

## Bidang fungsional menurut bentuk

| Jenis/bentuk | Data penting | Pendekatan |
| --- | --- | --- |
| Label datar | Ukuran potong, sudut, orientasi dan area aman | Reflow kolom/jarak bila rasio berubah; sesuaikan background. |
| Label wrap botol/jar silinder | Keliling di area tempel, tinggi bidang lurus, gap atau overlap | Ikuti permukaan tempel nyata dan posisikan sambungan di luar informasi penting. |
| Botol meruncing/kerucut/berlekuk | Ukuran batas atas/bawah label, tinggi/kemiringan dan pola | Bisa memerlukan pola lengkung; jangan meregangkan persegi panjang. Minta dieline/ukuran pembentuk pola yang masih kurang. |
| Dus lipat/karton | Panel, kedalaman, flap, tab lem, potong/lipat dan arah baca | Pertahankan geometri rangka dan susun per panel. Jangan mengasumsikan empat sisi sama lebar. |
| Pouch/sachet/bag | Depan/belakang, gusset, segel, zipper, takik dan bidang cetak | Ikuti bidang cetak yang diberikan. Foto depan tidak menentukan gusset atau area segel. |
| Sleeve/band/wrap | Bentangan, lipatan, overlap, muka yang tertutup | Cocokkan tampilan tiap muka dan sambungan setelah dilipat. |
| Bulat/oval/kontur/segel/tutup | Garis potong, pusat, bentuk dan area aman | Komposisi mengikuti kontur; sudut bounding box bisa berada di luar bidang sebenarnya. |
| Tube/cup/tray/blister/shrink sleeve/struktur khusus | Dieline/development pemasok dan batas dekorasi | Pakai template pembentuk yang sesuai. Kompensasi shrink/distorsi membutuhkan data khusus; mockup bukan pola produksi terverifikasi. |

Ini contoh, bukan daftar tertutup. Pada bentuk baru, identifikasi bidang fisik, batas sambungan, orientasi dan kebutuhan produksinya. Untuk konsep visual saja, jangan menghambat dengan data manufaktur yang belum dibutuhkan; jelaskan batas konsep itu.

## Silinder dan uji tempel

Keliling silinder `C = πd`, dengan diameter `d` pada area tempel. Panjang label dapat berupa `C - gap` atau `C + overlap`, sesuai keputusan pengguna; keduanya bukan tujuan yang dihitung bersamaan. Tinggi label mengikuti bidang tempel, bukan tinggi keseluruhan botol.

Jika panjang cetak sudah sesuai tetapi masih ada celah, ukur keliling pada permukaan yang benar-benar ditempeli, termasuk stiker lama jika tetap digunakan. Jangan memastikan penyebab hanya dari diameter nominal. Gunakan pengukuran itu untuk revisi dan uji satu cetakan pada Actual Size/100%.

```text
python scripts/layout_geometry.py cylinder --diameter 57 --height 51 --overlap 3
```

Helper menghitung silinder ideal; ia tidak mengetahui taper, bahu botol, toleransi, bahan atau keliling aktual.

## Rasio berbeda: pilih fit, crop atau reflow

1. Ukur batas artwork setelah memisahkan margin kosong/area non-artwork. Bandingkan rasio sumber `w/h` dengan target `W/H`.
2. Skala seragam `min(W/w, H/h)` memuat seluruh artwork dengan ruang tersisa. Skala seragam `max(W/w, H/h)` memenuhi bidang dengan crop, hanya jika bagian yang terpotong boleh hilang.
3. Jika rasio berbeda, tidak mungkin sekaligus mempertahankan seluruh komposisi persis, memenuhi semua tepi, dan menjaga proporsi tanpa ruang tambahan, crop atau reflow. Tanyakan pilihan konkret jika pengguna belum menetapkannya. Jangan diam-diam memilih skala X/Y berbeda.
4. Untuk reflow, pindahkan kelompok bermakna: brand/judul, foto, paragraf, tabel, logo/kode dan batch. Atur jarak/kolom; teks/logo/foto/kode tetap proporsional. Background/bar sederhana boleh diperpanjang. Reflow bukan izin mengganti isi, warna merek atau aset yang disetujui.
5. Jika bidang menyempit, pertimbangkan baris, kolom, margin atau orientasi sebelum mengecilkan teks melewati keterbacaan yang dibutuhkan. Jika informasi wajib tidak muat, sampaikan konflik; jangan menghapusnya demi tampilan.
6. Periksa hasil pada ukuran penempatan dan ukuran PDF ekspor. Ukuran native yang benar belum menjamin MediaBox/TrimBox PDF benar setelah pembulatan atau ekspor bleed.

Helper read-only memberi ukuran dalam mm, fit/cover dan sisa/crop; tidak mengubah file atau memilih desain:

```text
python scripts/layout_geometry.py fit --source-width 18 --source-height 10 --source-unit cm --target-width 18.2 --target-height 5.1 --target-unit cm
python scripts/layout_geometry.py fit --source-width 2400 --source-height 1200 --source-unit px --source-dpi 300 --target-width 150 --target-height 80
```

## Varian, gaya dan media

Pisahkan hal tetap dari hal berubah. Identitas merek, hierarki dan perlakuan foto bisa konsisten; paragraf, bahasa, isi, perusahaan, kode, warna varian, ukuran dan struktur dapat berbeda. Periksa tiap bidang berbeda; satu master ukuran tidak otomatis berlaku untuk seluruh varian.

Ikuti gaya/brief pengguna, bukan satu formula desain. Pada kemasan baru, jangan mewariskan klaim, komposisi, dosis atau sertifikasi dari makanan, kosmetik, herbal, produk rumah tangga maupun proyek lain yang tidak sesuai. Pada media kecil, periksa keterbacaan; pada media besar, resolusi efektif serta jarak baca. Font dan outline satu ukuran belum tentu cocok pada ukuran lain.

## Perubahan ukuran aktual dan varian isi

**Koreksi hasil pengukuran:** tentukan bidang yang dimaksud. Panjang badan dus berbeda dari bentangan termasuk flap, ukuran artboard, dan panjang label botol. Bila ukuran baru jelas merujuk ke satu dimensi badan, ubah dimensi itu dan sambungannya; jangan ikut mengubah label atau penampang dus yang tidak diminta. Jika dimensinya ambigu, tanyakan sebelum mengubah rangka.

Sesuaikan seluruh panel badan yang membentuk panjang tersebut, posisi garis lipat, flap penutup dan tab terkait. Panjang badan boleh dipendekkan sementara lebar flap dan bevel tetap dipertahankan dengan menggeser titik/ujung yang tepat; jangan meratakan seluruh rangka menggunakan skala X/Y yang merusak bagian lainnya. Simpan layer rangka revisi terpisah bila dokumen memang memakai layer panduan. Pertahankan sumber rangka awal sebagai referensi, dan bedakan ukuran awal dari revisi aktif pada catatan proyek.

Susun ulang jarak objek pada bidang yang menyempit. Pertahankan ukuran teks/kode yang masih muat; logo atau gambar boleh dikecilkan proporsional seperlunya. Ukur panel hasil native dan PDF, periksa sambungan/flap, lalu pastikan bidang lain yang tidak diminta berubah tetap sesuai. Sebutkan Actual Size / 100% saat menyerahkan PDF untuk uji ukur cetak.

**Varian isi baru:** jumlah isi tidak menentukan ukuran fisik secara otomatis. Periksa rangka/aset yang tersedia, lalu tanyakan apakah ukuran dus dan label tetap sama bila belum dinyatakan. Jika pengguna menyatakan “ukuran sama”, pakai dimensi revisi terakhir yang disetujui, bukan rangka sumber sebelum koreksi.

Pastikan komposisi varian dari sumber atau jawaban pengguna. Jika hanya volume total yang berubah, hasil hitung berdasarkan rasio lama boleh ditawarkan untuk dikonfirmasi; jangan langsung menganggap jumlah bahan, formula, atau dosis ikut berubah proporsional. Pastikan juga nomor TR untuk varian baru bila belum disetujui. Produsen dan istilah kolom yang sudah diputuskan dalam rangkaian proyek ini tetap berlaku kecuali ada informasi baru yang bertentangan.

Simpan varian dalam folder dan master terpisah dengan nama jenis desain, produk serta isi aktual sesuai SKILL.md. Gunakan ulang bahan gambar yang sudah disetujui; generasi ulang tidak diperlukan untuk perubahan volume/teks saja. Perbarui semua tempat yang menyebut isi: nama file, judul artboard, netto/isi, judul komposisi, jumlah bahan, bahan teks, manifest, PDF, preview dan indeks. Jangan mengganti angka umum dengan pencarian global yang dapat merusak dosis, nomor TR, tanggal atau metadata gambar. Pastikan angka varian lama tidak tertinggal pada artwork final; referensi historis tetap boleh memuat angka asal dengan penjelasan.

Periksa overflow setelah mengganti teks, termasuk angka yang lebih panjang. Untuk varian dengan ukuran tetap, verifikasi geometri dan proporsi objek tidak berubah. Pertahankan versi sebelumnya dan satu tautan yang jelas untuk setiap varian. Jangan menyalin preview atau laporan pemeriksaan varian lama sebagai bukti pemeriksaan varian baru.

## Pemeriksaan sesuai keluaran

- **Bahan**: aset terpisah, alpha/background benar, teks setia dan sumber tercatat. Tidak perlu mengklaim ukuran jadi yang belum ada.
- **Master editable**: pembagian objek sesuai kesepakatan, panel/orientasi benar, tidak ada overflow atau elemen tersembunyi yang keliru.
- **Cetak**: periksa ukuran/unit ekspor, skala 100%, trim/bleed/area aman yang telah ditentukan, resolusi efektif, profil warna yang diminta dan integritas kode. Bentuk QR persegi bukan bukti dapat dipindai; uji pembacaan bila tersedia dan relevan.
- **Mockup**: ikuti bentuk/kesan bahan, tetapi jangan menyamakan render 3D dengan validasi dieline, kemampuan produksi atau kecocokan fisik.
