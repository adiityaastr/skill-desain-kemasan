---
name: kemasan-desain
description: Siapkan, adaptasikan, dan revisi desain kemasan berbagai bentuk serta ukuran dari referensi atau brief. Gunakan untuk label, dus, pouch, sachet, sleeve, dieline, pemisahan aset/teks, dan penyusunan di Affinity bila diminta; bukan instalasi n8n atau otomasi server.
---

# Desain dan Bahan Kemasan

Sesuaikan pekerjaan dengan produk, media, bentuk, ukuran, gaya dan keluaran yang diminta. Jangan memakai ukuran, jumlah panel, warna, klaim, merek atau aset perusahaan dari proyek sebelumnya sebagai nilai bawaan. Kerjakan melalui tool yang tersedia, gunakan bahasa pengguna, dan berikan tautan hasil yang jelas. Jangan mengarahkan ke n8n/API berbayar kecuali diminta atau menjanjikan kemampuan tool yang belum diperiksa.

## Pilih cakupan dan sumber acuan

- **Scan bagian tertentu**: transkripsikan setia, siap salin. Tidak perlu gambar atau ZIP baru.
- **Siapkan bahan/background**: pisahkan aset, jangan hanya mengirim gambar kemasan utuh. Jumlah dan urutan mengikuti permintaan serta bidang aktual; empat sisi bukan aturan untuk semua kemasan. Sebutkan asumsi teks/logo dihapus dan dekorasi dipertahankan bila mengekstrak background.
- **Revisi aset**: ubah aset dan penempatannya yang relevan dalam proyek tersebut, bukan otomatis mendesain ulang seluruh kemasan.
- **Ubah ukuran/adaptasi bentuk**: baca [references/packaging-adaptation.md](references/packaging-adaptation.md). Bedakan halaman, artwork, ukuran jadi, bleed dan bidang cetak. Mengubah ukuran halaman saja belum tentu menyesuaikan artwork.
- **Desain baru**: ikuti brief dan gaya merek. Jika gaya belum ditentukan, pilih arah visual yang masuk akal dan jelaskan asumsi; jangan mengada-adakan dimensi produksi, identitas perusahaan, isi wajib, nomor atau klaim produk.
- **Buat/update di Affinity**: baca [references/affinity-layout.md](references/affinity-layout.md), gunakan rangka/dokumen yang dipilih dan pertahankan edit pengguna.
- **Perbarui aset di banyak desain**: inventarisasi master terbaru dan varian aktual sebelum mengedit. Untuk logo perusahaan, ikuti alur pembaruan massal di [references/company-logos.md](references/company-logos.md); jangan membatasi pencarian pada proyek yang terakhir dibuka.
- **Buat varian isi/gramasi**: gunakan desain terbaru yang disetujui sebagai dasar salinan terpisah. Pastikan ukuran fisik tetap atau berubah, komposisi varian dan nomor TR sebelum mengubah data terkait; lihat [references/packaging-adaptation.md](references/packaging-adaptation.md). Keputusan produsen dan format kolom yang sudah berlaku untuk rangkaian revisi yang sama tidak perlu ditanyakan ulang.
- **Gabungkan kemasan/varian**: aset dapat dipakai bersama jika sesuai, tetapi ukuran, teks, perusahaan, jumlah isi dan keluaran tiap varian tetap diperiksa sendiri. Paket bahan bukan otomatis permintaan desain final atau izin mengubah semua proyek lama.

Periksa sumber terbaru: muat gambar lokal sebelum edit, baca ukuran dari dokumen/rangka yang nyata, lihat batas artwork dan anotasi. Cari aset/revisi yang sudah disetujui sebelum membuat ulang. Untuk bahan saja, ukuran fisik boleh belum ada; untuk cetak atau adaptasi struktural, jangan menebaknya dari screenshot.

## Ringkas spesifikasi yang memengaruhi hasil

Ambil informasi dari file dan percakapan terlebih dahulu. Catat seperlunya: produk/varian, jenis kemasan, ukuran dan satuan, bidang/panel, arah baca/lipat, gaya/acuan, bagian yang boleh berubah, bagian yang dipertahankan, serta keluaran. Ini catatan kerja, bukan formulir panjang yang harus diisi pengguna setiap kali.

Instruksi terbaru menentukan tujuan; rangka dan spesifikasi percetakan menentukan geometri produksi dalam cakupannya. Jika keduanya bertentangan, jelaskan konflik dan pastikan keputusan sebelum mengubah geometri. Jangan diam-diam mengganti bentuk, unit, profil warna, skala atau bleed untuk menyembunyikan ketidakcocokan. Tanyakan informasi yang hilang hanya bila berpengaruh pada tugas; ukuran label tidak diperlukan untuk scan satu paragraf.

Sebelum mulai menyiapkan bahan atau menyusun desain, pastikan nomor registrasi/TR yang akan dipakai. Jika pengguna belum menentukan nomornya untuk proyek ini, tanyakan secara spesifik; nomor pada master lama bukan otomatis persetujuan untuk dipakai lagi. Jika sumber memuat XXX atau berbeda antarversi, jelaskan pilihan sumber dan tunggu keputusan untuk bagian yang bergantung padanya. Jika CV/PT atau identitas produsen berbeda antaracuan dan belum diputuskan pengguna, tanyakan juga. Jangan menanyakan ulang nomor/perusahaan yang sudah jelas ditetapkan pada proyek yang sama.

Jika desain memuat kolom nomor produksi dan kedaluwarsa, sebelum menyiapkan teks/layout tanyakan format yang diinginkan bila belum ditentukan: **format lama `Batch No` / `Exp Date` atau format baru `Kode Produksi` / `Kedaluwarsa`?** Jangan otomatis mengikuti istilah pada referensi atau proyek terdahulu. Setelah pengguna memilih, terapkan konsisten pada seluruh inner/label yang memuat kolom tersebut, bahan teks, master, PDF dan preview; periksa ulang agar label yang lebih panjang tetap muat. Jangan menanyakan kembali keputusan yang sudah diberikan untuk proyek yang sama dan jangan menambahkan kolom yang tidak diminta hanya untuk memakai format ini.

## Pisahkan gambar, teks dan bentuk

Buat daftar komponen seperlunya: nama, jenis, sumber, bidang penempatan, status kesiapan dan aturan skala. Utamakan objek asli pada PDF/AI/CDR bila dapat diekstrak; bedakan `extracted` dari `reconstructed`.

- **Teks editable**: informasi produk, nama, komposisi, petunjuk dan manfaat, termasuk tulisan di dalam kuas/lingkaran. Kedekatan dengan ilustrasi tidak menjadikannya bagian gambar.
- **Gambar**: foto, ilustrasi, pita, sapuan kuas, logo dan ikon boleh tetap bitmap jika lebih setia pada sumber. Logotype khusus dapat tetap gambar; jangan menjadikannya alasan meratakan seluruh informasi kemasan.
- **Bentuk/layout**: panel, bar, kotak batch, gradasi, garis dan rangka cocok sebagai bentuk native/SVG. Bitmap dibungkus SVG bukan hasil tracing vektor.

Jika ragu suatu bagian adalah gambar, tulisan, background, lubang transparan atau elemen yang tumpang tindih, **tanyakan pembagian yang konkret sebelum generate, menghapus, merekonstruksi atau menggabungkan bagian tersebut**. Misalnya: “Pita dan kuas dipisah menjadi dua gambar, sedangkan nama serta manfaat menjadi teks editable?” Jangan generate untuk menebak maksud pengguna. Tunggu jawaban untuk pekerjaan yang bergantung pada keputusan itu; diam bukan persetujuan. Jangan menanyakan kembali keputusan yang sudah jelas pada revisi berikutnya.

Alur lengkap: **siapkan/pisahkan bahan → bersihkan atau pertajam bila perlu → periksa bahan → susun → periksa hasil gabungan**. Bila pengguna meminta mengulang dari gambar, analisis kembali gambar dan siapkan komponen terpisah sebelum merakit dokumen baru dari rangka; menyalin atau menyimpan ulang master lama saja tidak memenuhi permintaan itu. Aset yang sudah benar boleh dipakai kembali sesuai cakupan, dengan asalnya dicatat. Revisi satu aset tidak memerlukan pengulangan seluruh alur. Bila Affinity diminta hanya untuk penggabungan, selesaikan pengolahan bitmap sebelum penempatan.

## Adaptasi ukuran, bentuk dan gaya

Pakai geometri aktual, bukan asumsi bahwa semuanya kotak atau mempunyai empat panel. Label botol, dus, pouch, segel bundar, sleeve dan struktur khusus memiliki batas berbeda; lihat [references/packaging-adaptation.md](references/packaging-adaptation.md).

Skalakan tulisan, logo, foto, ilustrasi, QR dan barcode secara proporsional. Bila rasio target berbeda, atur ulang jarak, kolom, ukuran teks yang masih terbaca dan background sesuai cakupan; jangan meregangkan seluruh artwork. Bentuk dekoratif/background boleh mengikuti bidang baru jika maknanya tidak berubah. Jika reflow/crop akan mengubah desain yang diminta tetap sama, pastikan pilihan pengguna dahulu.

Gaya mengikuti brief: mewah, minimalis, tradisional, ceria, teknis atau gaya lain bukan template tetap. Pertahankan hierarki merek dan detail yang diminta sambil menyediakan ruang untuk informasi wajib. Jangan mewariskan komposisi, klaim, dosis, sertifikasi atau identitas perusahaan dari produk lain hanya karena layoutnya mirip.

Helper read-only menghitung rasio, fit/cover dan keliling silinder; tidak mengubah desain atau menentukan struktur produksi:

```text
python scripts/layout_geometry.py fit --source-width 158.338 --source-height 54.529 --target-width 182 --target-height 51
python scripts/layout_geometry.py cylinder --diameter 5.7 --unit cm --overlap 0.3
```

## Isi dan aset yang setia pada sumber

Pertahankan ejaan, angka, satuan, nama Latin, petunjuk, produsen, distributor dan nomor sesuai sumber. Pada tugas scan, jangan diam-diam memperbaiki ejaan. Tandai `[tidak terbaca]` daripada melengkapi angka dari ingatan. Pada desain baru, minta isi yang diperlukan atau tandai placeholder; jangan mengarang klaim/regulasi. Cap ACC dan persetujuan pada referensi biasanya anotasi, bukan artwork baru. Jangan menambahkan isi dari inner ke label yang tidak memuat bagian tersebut tanpa permintaan.

Jangan mengklaim font persis hanya karena mirip. Jelaskan font pendekatan bila font asli tidak tersedia. Sertakan font/lisensi hanya bila tersedia dan berguna.

Untuk edit/generasi bitmap, ikuti instruksi imagegen/tool yang berlaku; skill ini tidak memberi izin backend alternatif. Penajaman generatif dapat mengubah detail: simpan sumber dan catat rekonstruksi. Jika pengguna memilih metode teknis tanpa AI, terapkan pada rangkaian revisi aset yang sama tanpa bertanya ulang; ini bukan izin umum untuk semua pekerjaan berikutnya.

Logo sertifikasi serta QR/barcode berasal dari aset pengguna/penerbit yang sesuai. Logo halal dapat berasal dari perusahaan atau pemilik sertifikat mana pun; tidak ada perusahaan pilihan bawaan. Tentukan pemilik sertifikat yang relevan dari sumber proyek dan instruksi pengguna, bukan sekadar merek, distributor, kemiripan nama, atau proyek sebelumnya. Jika hubungan pemilik sertifikat dengan produk/produsen belum jelas, tanyakan sebelum memasang logo. Jangan generate nomor atau kode yang tampak valid. Utamakan aset yang sudah disesuaikan pengguna dan cocokkan perusahaan/produk/variannya. Baca [references/company-logos.md](references/company-logos.md) untuk pencocokan pemilik sertifikat dan pengelolaan pustaka logo proyek.

Untuk transparansi, outline, kuas/pita, background dan tepi panel, baca [references/image-editing.md](references/image-editing.md) saat relevan. Periksa sumber bidang yang meragukan: kuas yang terlihat lewat lubang pita bisa tampak seperti lipatan pita. Jangan memasukkan anotasi merah pengguna ke artwork.

## Pemeriksaan ulang sebelum penyerahan

Periksa hasil aktual yang tersimpan, bukan hanya suksesnya tool. Render/export hasil gabungan setelah perubahan terakhir dan buka gambar hasil. Pilih pemeriksaan yang sesuai tugas:

1. **Geometri**: ukuran fisik/unit benar; artwork sesuai bidang; panel, lipatan, flap, tab lem, area segel, lubang dan sambungan mengikuti rangka. Proporsi elemen tidak berubah tanpa dasar. Periksa ukuran halaman PDF ekspor, bukan hanya ukuran native.
2. **Isi/komponen**: varian, jumlah isi, teks, angka, satuan, perusahaan dan nomor cocok. Teks yang disepakati editable benar-benar terpisah. Edit dan QR pengguna pada dokumen aktif tetap ada.
3. **Gambar**: logo utuh; alpha termasuk rongga/celah benar; tidak ada matte, checkerboard tercetak, halo, bintik, potongan atau detail hilang. Lihat pada ukuran penempatan. Outline memenuhi revisi sambungan tanpa menutup rongga utama.
4. **Layout**: teks terbaca, tidak overflow/tertutup; kode tidak terdistorsi atau bertabrakan; arah baca benar. Ukur bar yang harus sejajar atau menempel tepi; jangan menyatakan persis sejajar hanya dari persentase prompt.
5. **Versi/paket**: seluruh penempatan memakai aset terbaru; master, PDF, preview, bahan, catatan dan ZIP berasal dari revisi sama; tautan benar. Cocokkan logo/perusahaan dan seluruh digit nomor dari sumber sampai penempatan.

Perbaiki kesalahan yang jelas dalam cakupan lalu periksa bagian terdampak. Jika hasil benar masih ambigu, tanyakan keputusan yang diperlukan. Jika pemeriksaan tidak dapat dilakukan, laporkan batasnya; jangan mengklaim tervalidasi atau siap cetak secara menyeluruh. Setelah pemeriksaan relevan lulus, hentikan pengulangan yang tidak diperlukan. Jika dua generasi gagal dengan artefak serupa, ubah strategi yang diizinkan atau jelaskan kendalanya; jangan mengulang janji bahwa hasil sudah bersih.

Helper inspeksi gambar yang tidak mengubah berkas:

```text
python scripts/package_assets.py inspect "path/to/panel-1.png" "path/to/panel-2.png"
```

## Simpan dan serahkan

Simpan hasil di proyek pengguna, bukan hanya staging generator/Desktop. Jangan menimpa sumber. Susun folder sesuai keluaran: aset bersama, bagian/varian, teks, master, preview dan referensi; jangan memaksakan folder dus/label untuk setiap jenis kemasan. Gunakan identitas revisi yang jelas dan satu penunjuk master terbaru dalam indeks paket.

Sebelum memberi nama file, **periksa desain yang benar-benar tersedia pada referensi dan dokumen aktual**. Jangan menganggap setiap proyek berisi inner sekaligus label. Tentukan jenis berdasarkan artwork yang ada dan cakupan keluaran:

- Inner saja: `INNER {NAMA PRODUK} {UKURAN GRAMASI}`.
- Label saja: `LABEL {NAMA PRODUK} {UKURAN GRAMASI}`.
- Inner dan label digabung dalam satu file: `INNER DAN LABEL {NAMA PRODUK} {UKURAN GRAMASI}`.

Jika inner dan label diserahkan sebagai file terpisah, namai masing-masing sesuai isinya; keberadaan dua jenis dalam folder tidak menjadikan setiap file bernama `INNER DAN LABEL`. Jika jenis artwork belum jelas setelah diperiksa, tanyakan kepada pengguna sebelum menentukan nama atau membuat bagian yang tidak tersedia. Untuk jenis kemasan lain, gunakan jenis aktual yang sesuai brief; jangan memaksakan kategori inner/label.

Ambil nama produk, jumlah isi dan satuan dari spesifikasi aktual; jangan mengubah kapsul/sachet/ml menjadi gram atau mengarang berat. Untuk varian selain gram, isikan bagian ukuran dengan jumlah/ukuran isi yang benar, misalnya `30 CAPS` atau `20 SACHET`. Contoh: `INNER BENODEM 30 CAPS.af`, `LABEL CARDIMAX 280 G.af`, atau `INNER DAN LABEL BENODEM 30 CAPS.af` bila memang memuat keduanya. Gunakan nama dasar yang sama pada master dan ekspornya. Letakkan identitas revisi pada folder/indeks agar nama file tetap mengikuti format pengguna. Jangan mengganti nama file sumber atau file lama secara massal kecuali diminta.

Serahkan folder desain sebagai keluaran utama. **Jangan otomatis membuat ZIP setelah folder selesai. Buat ZIP hanya bila pengguna memintanya.** Kata “paket” atau tersedianya helper ZIP bukan permintaan kompresi.

Catat asal aset sebagai `source`, `extracted`, `reconstructed`, atau `unspecified`, metode dan batasnya. Format catatan ada di [references/package-format.md](references/package-format.md). Hanya jika ZIP diminta, gunakan helper berikut:

```text
python scripts/package_assets.py package "path/to/staging" --output "path/to/paket-v2.zip"
```

Helper membuat manifest hash dan ZIP baru, tidak menimpa ZIP lama atau mengubah staging. Masukkan hanya bahan yang diserahkan. Revisi harus disertai PDF/preview mutakhir bila keluaran itu ikut diserahkan; perbarui ZIP hanya jika ZIP memang diminta sebagai keluaran revisi tersebut. Untuk scan satu bagian, cukup transkripsinya.

Jawaban akhir ringkas: hasil, tautan utama dan keterbatasan yang berdampak, misalnya font pendekatan, dimensi belum terkonfirmasi atau format warna belum sesuai permintaan percetakan. Jangan menjanjikan semua ukuran/jenis kemasan pasti siap produksi tanpa data dan pemeriksaan yang diperlukan.
