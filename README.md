# Bike Sharing Dashboard
## Persyaratan
Sebelum menjalankan dashboard, pastikan Anda telah menginstal dependensi berikut:
- Python
- Streamlit
- Pandas
- Numpy
- Matplotlib
- Seaborn
### Instalasi Dependensi
Jika belum terinstal, menginstalnya dengan perintah ini:

```sh
pip install streamlit pandas matplotlib seaborn
```

## Cara Menjalankan Dashboard
1. Pastikan file `dashboard.py` dan dataset (`day_data.csv`, `hour_data.csv`) berada dalam folder yang sama.
2. Buka terminal atau command prompt, lalu arahkan ke folder tempat `dashboard.py` disimpan.
```sh
cd submission
```
```sh
cd dashboard
```
3. Jalankan perintah berikut:

```sh
streamlit run dashboard.py
```

4. Dan Dashboard akan terbuka di browser secara otomatis.

## Visualisasi yang ada di dashboard
Dashboard ini menampilkan beberapa visualisasi utama, yaitu:
- **Tren Penyewaan Sepeda**: Menampilkan pola peminjaman sepanjang tahun.
- **Peminjaman Berdasarkan Hari dalam Seminggu**: Menggambarkan rata-rata peminjaman untuk setiap hari dari Senin hingga Minggu.
- **Peminjaman Berdasarkan Jam**: Menampilkan jam-jam dengan jumlah peminjaman tertinggi dan terendah.


