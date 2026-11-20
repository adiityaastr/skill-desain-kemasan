# Format paket

Folder desain adalah keluaran utama. Jangan membuat ZIP secara otomatis; kompresi dilakukan hanya atas permintaan pengguna. Helper `package` membuat ZIP sehingga jangan menjalankannya sekadar untuk menyelesaikan folder desain.

Periksa isi desain sebelum penamaan. Master dan ekspor memakai `INNER {NAMA PRODUK} {UKURAN GRAMASI}` untuk inner saja, `LABEL {NAMA PRODUK} {UKURAN GRAMASI}` untuk label saja, dan `INNER DAN LABEL {NAMA PRODUK} {UKURAN GRAMASI}` hanya jika satu file memuat keduanya. File terpisah mengikuti isi masing-masing. Untuk kemasan lain, gunakan jenis aktual; jika jenisnya ambigu, tanyakan setelah memeriksa sumber. Gunakan isi/satuan aktual, misalnya `280 G`, `30 CAPS`, atau `20 SACHET`, dengan ekstensi yang diminta. Revisi dibedakan melalui folder dan indeks.

Staging hanya berisi bahan yang akan diserahkan. `ASSET-MANIFEST.json` dicadangkan untuk manifest otomatis. Helper menolak symlink, file environment, key dan ZIP bersarang. Ini pemeriksaan dasar, bukan pemindai rahasia lengkap.

Opsional: `provenance.json` dalam staging adalah mapping path relatif ke metadata:

```json
{
  "01-aset-bersama/logo/merek.png": {
    "origin": "reconstructed",
    "source": "04-referensi/label-asli.png",
    "method": "imagegen",
    "notes": "Rekonstruksi, bukan master logo asli."
  }
}
```

Origin yang diterima: `source`, `extracted`, `reconstructed`, `unspecified`. Script tidak menebak asal dari nama. Path memakai slash relatif; tidak perlu path komputer dalam metadata.

ZIP berisi setiap file, manifest path/byte/SHA-256 dan informasi gambar bila Pillow tersedia. Manifest tidak membuktikan keaslian logo, identitas font, sertifikasi atau kesiapan cetak.
