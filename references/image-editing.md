# Pemeriksaan gambar kemasan

Ikuti instruksi skill imagegen/tool yang berlaku. Ini spesifikasi hasil, bukan izin backend alternatif.

## Edit lokal

Contoh: ubah hanya tulisan SENESA menjadi putih solid, pertahankan emblem hijau/cyan, siluet huruf, jarak dan posisi. Alpha nyata; tanpa glow, halo, bayangan atau redesain. Simpan versi sebelumnya.

## Transparansi

Bedakan cutout objek (isi putih tetap opaque) dengan overlay tinta (putih di sela/di dalam objek ikut transparan). Untuk ilustrasi garis merah di atas bidang warna, overlay biasanya lebih berguna; nyatakan asumsi bila perlu.

Minta alpha nyata, tanpa red fog, colored halo, white matte atau checkerboard tercetak. Lihat hasil di atas bidang terang dan gelap bila tersedia. Alpha sudut 0 saja tidak menjamin seluruh background bersih.

Periksa juga lubang tertutup (contoh: tengah pita), celah persilangan dan celah antara ekor. Untuk permintaan penghapusan background, area kosong tersebut ikut transparan kecuali pengguna meminta bidang putih tetap opaque. Transparansi bukan warna putih, hitam, atau kotak-kotak yang dicetak pada RGB.

Bedakan **garis putih yang sengaja ditambahkan** dari **sisa white matte**. Setelah menghapus background, outline putih ditambahkan hanya bila diminta. Lubang besar tetap terbuka meskipun garis putih pada sambungan kecil dibuat bertemu.

Pada hasil AI, cari bintik magenta/putih di luar siluet dan di lubang tengah. Jangan menganggapnya sekadar tampilan preview: periksa alpha dan warna piksel jika perlu. Setelah dua kegagalan serupa, pilih strategi lain yang diizinkan atau jelaskan kendalanya, bukan mengulang janji bahwa hasil sudah bersih.

Jika pengguna sudah memilih metode teknis tanpa AI, mulai dari PNG sumber bersih, bukan hasil AI yang terkena bintik. Untuk penghapusan putih, pertahankan warna ungu/warna objek pada interior, unmatte tepi seperlunya dan simpan alpha yang bersih. Jangan menghapus warna putih yang memang bagian objek tanpa melihat cakupan permintaan.

## Pisahkan kuas, pita dan tulisan

Jika belum yakin komponen mana yang harus dipisah atau seperti apa hasil akhirnya, ikuti aturan klarifikasi di `SKILL.md`: tanyakan pembagian yang konkret dan tunggu jawaban sebelum mengolah bagian itu. Jangan langsung generate dengan asumsi sendiri.

Asset kuas tidak boleh memuat tulisan nama produk/manfaat yang nantinya harus editable. Jangan sekadar menutup tulisan dengan kotak putih yang memotong sapuan kuas; periksa tepi kuas setelah pemisahan. Pisahkan pita dari sapuan lingkaran yang kebetulan terlihat di belakangnya.

Saat bidang pada lubang pita tampak salah, periksa dua hal: apakah bidang itu tertanam dalam PNG pita atau merupakan layer kuas di belakang yang terlihat melalui alpha. Menghapus bidang dari PNG saja tidak menyelesaikan masalah layer belakang. Sebaliknya, jangan mengisi lubang dengan putih opaque diam-diam saat pengguna meminta transparansi. Pertahankan alpha dan atur elemen belakang hanya sesuai revisi yang diminta.

## Outline putih

Tambahkan outline dari alpha aset yang sudah bersih, di belakang warna objek. Pertahankan bentuk dan warna interior; jangan memperbesar bidang ungu untuk meniru outline. Ukur ketebalan dalam piksel aset dan lihat hasil pada ukuran penempatan sebenarnya: stroke yang tampak tebal pada PNG besar bisa terlalu tipis pada label kecil.

Untuk revisi “sedikit dipertebal hingga garis putih bertemu”, tingkatkan ketebalan secara bertahap sampai celah sempit pada sambungan terjembatani. Periksa visual sambungan dan lubang; jangan menutup rongga utama. Angka ketebalan mengikuti resolusi dan skala penempatan, bukan nilai tetap untuk semua produk.

Simpan PNG versi baru dengan nama jelas, lalu ganti semua penempatan aset terkait di dus dan label. Jangan menyatakan file Affinity sudah diperbarui bila baru PNG yang berubah.

## Background

Pisahkan bidang badan dari flap; gunakan jumlah file sesuai permintaan. Hilangkan teks, logo, QR, garis dieline, cap dan teks persetujuan. Pertahankan ilustrasi dekoratif jika dimaksud sebagai background. Untuk label wrap, rasio memakai bidang label saja, tanpa header di luar artwork.

## Bar dan sudut

Tetapkan satu acuan width/height dan koordinat bar. Contoh: jika panel acuan 823x1910 memiliki batas kuning y=1803, panel sebelah harus memakai ukuran dan batas tersebut untuk klaim sejajar piksel. Persentase prompt saja bukan verifikasi.

Bidang merah pojok harus mencapai tepi kanan dan bawah bila diminta menempel sudut. Jangan meninggalkan strip putih/kuning. Hindari crop seluruh gambar untuk menutup gap lokal bila memengaruhi komposisi.

## Keaslian

Penajaman generatif bisa mengubah bentuk huruf. Tandai rekonstruksi dan simpan sumber. Untuk tanda sertifikasi dan QR, gunakan sumber sahih; jangan memulihkan detail kecil dengan tebakan.
