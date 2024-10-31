
# Task Home Regtech

## Deskripsi Proyek

Proyek ini bertujuan untuk melakukan web scraping pada situs Vessel Finder untuk mengambil informasi kapal secara otomatis. 
Data kapal ini meliputi nama kapal, tipe, estimasi waktu kedatangan (ETA), jarak/waktu, arah/kecepatan, draught saat ini, 
status navigasi, posisi diterima, informasi IMO/MMSI, panggilan sinyal, bendera, serta panjang/lebar kapal. 
Data ini disimpan dalam format CSV setelah diambil dari beberapa halaman situs.

## Persyaratan

- Python 3.x
- `selenium`
- `pandas`
- Google Chrome dan ChromeDriver

## Struktur Kode

Kode ini menggunakan Selenium WebDriver untuk mengontrol peramban dan mengakses halaman Vessel Finder, kemudian mengumpulkan 
data kapal dari halaman utama serta halaman detail. Setelah data dari beberapa halaman diambil, data disimpan dalam file CSV.

## Penggunaan

1. **Instalasi dependensi**:
   Pastikan `selenium` dan `pandas` sudah terinstal. Jika belum, jalankan perintah berikut:
   ```bash
   pip install selenium pandas
   ```

2. **Download ChromeDriver**:
   Unduh versi [ChromeDriver](https://sites.google.com/chromium.org/driver/) yang sesuai dengan versi Google Chrome Anda. 
   Tentukan path menuju file ini pada variabel `path` di kode.

3. **Menjalankan kode**:
   Setelah ChromeDriver siap dan diatur, jalankan skrip dengan:
   ```bash
   python nama_file_script.py
   ```

4. **Data Output**:
   File CSV dengan data kapal akan disimpan di path yang ditentukan dalam kode.

## Output

File output yang dihasilkan berisi kolom-kolom sebagai berikut:
- Nama Kapal
- Tipe Kapal
- Prediksi ETA
- Jarak / Waktu
- Arah / Kecepatan
- Draught Saat Ini
- Status Navigasi
- Posisi Diterima
- IMO / MMSI
- Panggilan Sinyal
- Bendera
- Panjang / Lebar

## Catatan

Pastikan koneksi internet stabil saat menjalankan kode ini, serta sesuaikan durasi waktu tunggu (wait time) sesuai dengan kecepatan 
internet untuk menghindari error saat memuat halaman.

## Lisensi

Proyek ini bersifat terbuka untuk digunakan dalam pembelajaran dan pengembangan, tanpa jaminan apa pun.
