# Penyusunan dan revisi di Affinity

Baca saat pengguna meminta desain native Affinity atau memperbarui aset pada file tersebut, untuk jenis kemasan apa pun. Gunakan daftar bidang/panel aktual; contoh dus dan label di bawah bukan batas jenis yang didukung. Untuk ukuran/bentuk yang berubah, baca [packaging-adaptation.md](packaging-adaptation.md). Persiapan/penajaman gambar tetap mengikuti metode yang dipilih pengguna dan aturan tool gambar; alur ini tidak menjadi pengecualian untuk backend edit bitmap.

## Sebelum menggabungkan

Gunakan rangka/file yang diminta, bukan perkiraan ukuran dari JPG. Jika pengguna menyebut ukuran sama dengan proyek sebelumnya, periksa bidang panel, label dan flap pada file native tersebut. Simpan salinan baru agar sumber tetap tersedia.

Siapkan bahan final terlebih dahulu: gambar bersih dan cukup tajam, alpha diperiksa, teks ditranskripsikan, serta background per sisi sejajar. Jangan memaksa semua ilustrasi menjadi vektor. Nama produk/manfaat yang berada di dalam kuas tetap merupakan teks terpisah kecuali pengguna meminta perlakuan logo khusus.

## Pilih dokumen yang benar

Periksa dokumen yang sedang aktif, judul, path dan status salinan. Bisa ada beberapa dokumen dengan judul sama di Desktop dan workspace. Jangan memilih dokumen pertama yang judulnya cocok lalu mengabaikan revisi pengguna pada salinan aktif. Jika dokumen sudah ditutup, buka versi tersimpan terbaru yang relevan.

Pertahankan edit pengguna di luar cakupan. Tanda merah koreksi bukan artwork: identifikasi layer anotasinya secara visual, lalu sembunyikan secara reversibel bila sesuai dengan revisi. Jangan menyembunyikan semua layer bernama `Pixel` tanpa memastikan isinya.

Jika dokumen aktif memiliki perubahan yang belum tersimpan, gunakan keadaan aktif sebagai dasar revisi dan simpan ke salinan baru. Jangan menggantinya dengan salinan staging atau file tersimpan yang lebih lama hanya karena judulnya sama. Contohnya, QR yang ditambahkan pengguna harus tetap ada saat mengganti logo halal, walaupun referensi JPG lama hanya berisi kotak putih. Periksa QR pada dokumen aktual; jangan mengembalikannya menjadi placeholder atau membuat QR pengganti. Cocokkan pula isi paket dan catatan hasil dengan keadaan terbaru ini.

## Layer dan penggantian aset

- Pisahkan grup per sisi dus, label, gambar dan teks yang bermakna.
- Tempatkan gambar pada skala proporsional. Jangan memperlebar/memanjangkan pita agar muat tanpa dasar dari sumber.
- Gunakan PNG ber-alpha langsung untuk aset transparan. Jangan meninggalkan bidang putih atau clipping lama yang menutup lubang.
- Untuk revisi pita/ikon, cari seluruh penempatannya, simpan posisi dan ukuran, lalu ganti dengan revisi terbaru. Contoh satu pita dapat dipakai pada dua panel dus dan label; hitung berdasarkan file, bukan selalu menganggap jumlahnya tiga.
- Untuk logo halal perusahaan, ikuti [company-logos.md](company-logos.md). Pertahankan skala proporsional: jika rasio aset baru berbeda, jaga satu dimensi atau batas area penempatan lalu sesuaikan dimensi lainnya. Periksa nomor di bawah logo dan ruang ke QR/teks di sekitarnya; jangan meregangkan logo agar persis mengisi kotak aset lama.
- Periksa tumpukan layer: bidang putih pada gambar kuas bisa menutup JAMU; kuas yang terlihat melalui lubang pita bisa tampak seperti lipatan tambahan. Penyelesaian harus mengikuti cakupan revisi, bukan menyembunyikan efek alpha dengan matte putih tanpa permintaan.
- Outline harus terlihat pada ukuran dus dan label. Periksa garis pada persilangan dan ujung, serta pastikan rongga utama tetap sesuai pilihan transparansi pengguna.

## Catatan MCP/SDK yang telah ditemui

Temukan tool yang tersedia, baca `preamble` dan dokumentasi SDK yang relevan. Cari hint sebelum bereksperimen dan catat solusi yang benar melalui tool hint. Contoh berikut adalah petunjuk implementasi, bukan pengganti pemeriksaan API versi berjalan:

- SDK dapat membatasi akses filesystem ke Desktop. Jika demikian, stage aset di Desktop lalu salin master tersimpan ke workspace. Jelaskan path salinan yang benar; jangan mengklaim salinan workspace sedang terbuka jika aplikasi masih membuka salinan Desktop.
- Setelah aplikasi dimulai ulang, koneksi MCP lama dapat macet meskipun aplikasi masih berjalan. Coba sambungan baru melalui bridge yang sudah dikonfigurasi, baca kembali preamble, lalu lakukan pemeriksaan read-only sebelum mutasi. Jangan menjalankan ulang mutasi yang status akhirnya belum diketahui, membunuh aplikasi yang mungkin menyimpan edit pengguna, atau mengubah konfigurasi global hanya untuk mengatasi koneksi sementara.
- Ukuran lokal node di dalam parent bertransformasi tidak selalu sama dengan ukuran di spread. Periksa bounding box aktual sesudah penempatan, lalu sesuaikan skala dan translasi terhadap koordinat spread. Proporsi logo harus benar pada hasil render, bukan hanya pada nilai lebar/tinggi lokal.
- `nodeId` dapat berupa BigInt; serialisasikan dengan `String(...)`.
- Pastikan spread tujuan aktif sebelum mengedit; jangan mengatur ulang spread yang sama tanpa perlu karena dapat menghapus selection.
- Bitmap dan `ImageNodeDefinition` harus memakai format yang kompatibel dengan dokumen. Dalam pekerjaan ini, RGB yang dimasukkan ke template CMYK dengan format salah pernah menghasilkan warna keliru/`COMMAND_FAILED`. Periksa render dan jangan menjanjikan master CMYK hanya karena template awal CMYK. Jika bekerja dalam RGB, catat format itu.
- Helper `RGB8(...)` menghasilkan `Colour`; `Colour.createRGBA8(...)` menerima struktur `{r,g,b,alpha}`, bukan array angka.
- Default frame text pada 300 dpi pernah memiliki `paragraphAtts.spaceAfter=50`. Tetapkan spacing dan leading dengan sengaja agar baris tidak meluber.
- Untuk mengatur selection aktif, gunakan setter `document.selection = nodeOrSelection`. Memutasi objek getter belum tentu mengubah selection UI/export.
- `document.setText(teks, node)` dapat menyisipkan teks pada caret/akhir story, bukan mengganti seluruh isi. Untuk mengganti label/angka, gunakan `Selection.create(document, node)` dengan `TextSelection.create([{begin: range.begin, end: range.begin + range.length}])` dari `node.storyInterface.storyRange`, lalu `addSubSelectionForNode` dan `document.setText(teks, selection)`. Periksa teks aktual agar istilah baru tidak menempel pada istilah lama dan cek overflow setelah penggantian.
- `saveAs` ke path dokumen yang sama pernah menghasilkan `BACKING_DATA_LOST`. Gunakan `save()` untuk path yang sama atau `saveAs()` ke path baru.

## Validasi dan penyerahan

Render hasil setelah penggantian. Periksa alpha, outline, layer tertutup, logo utuh, anotasi, angka isi kapsul dan text overflow. Pemeriksaan flow teks tidak menggantikan pemeriksaan tumpukan gambar secara visual.

Lakukan pemeriksaan ulang pada dua tingkat: halaman/panel secara utuh untuk komposisi dan penyelarasan, lalu detail aset yang direvisi pada ukuran penempatan untuk tepi, rongga dan sambungan. Cocokkan dengan instruksi terakhir pengguna; tampilan yang berbeda dari PNG tunggal dapat disebabkan oleh layer belakang, clipping atau urutan tumpukan.

Periksa versi yang benar-benar disimpan dan pratinjau yang diekspor setelah perubahan terakhir. Jika penyimpanan bermasalah atau ada keraguan tentang file native, pastikan salinan tersimpan dapat dibuka sebelum menyerahkannya. Setelah koreksi, render ulang bagian terdampak; jangan memakai pratinjau lama sebagai bukti revisi baru.

Untuk revisi banyak master, buka ulang salinan native tersimpan dan periksa jumlah aset baru serta ukuran/format dokumen. Jika path workspace ditolak SDK tetapi staging dapat dibuka, verifikasi native di staging dan kesamaan hash setelah disalin; laporkan lokasi file yang sedang terbuka secara akurat. Jangan mengklaim file workspace sudah berhasil dibuka bila mendapat `PERMISSION_DENIED`.

Simpan file native dan pratinjau terbaru ke workspace. Periksa isi dokumen sebelum menamai: gunakan awalan `INNER`, `LABEL`, atau `INNER DAN LABEL` sesuai artwork yang benar-benar ada dalam file, mengikuti aturan penamaan pada SKILL.md. Serahkan folder; jangan membuat ZIP otomatis. Berikan tautan ke master revisi yang jelas. Jangan membuat banyak versi bernama `final` tanpa penunjuk master terbaru; jika ZIP diperbarui, masukkan master dan bahan yang benar, bukan seluruh percobaan lama. Jangan mengatakan ZIP lama sudah mutakhir jika hanya PNG/native yang berubah.
