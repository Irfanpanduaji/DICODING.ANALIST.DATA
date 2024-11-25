# DICODING.ANALIST.DATA

## Penulis
- **Nama:** Irfan Pandu Aji
- **Email:** ( panduaji7972@gmail.com )
- **MyProfil Dicoding:** [ https://www.dicoding.com/users/irfanaji/academies ]

## Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```
## Berkas
- `Proyek_Analisis_Data.ipynb`: Notebook Jupyter yang berisi analisis data.
- `dashboard/`: Direktori yang berisi aplikasi dashboard Streamlit.

## Membuat File dashboard.py
- Notebook Jupyter dapat dilihat langsung di GitHub atau dijalankan dalam lingkungan yang mendukung Jupyter Notebook Python.
- Dashboard Streamlit dapat dijalankan secara lokal dengan terlebih dahulu menavigasi ke direktori dashboard/ dan menjalankan perintah berikut:
```
cd dashboard
streamlit run dashboard.py
```
## Menmbuka Folder dashboard.py di comand prompt anda dan run Streamlit
Pastikan Anda berada di folder dashboard terlebih dahulu sebelum menjalankan aplikasi Streamlit, karena file dashboard.py berada di dalam folder tersebut.
```
cd dashboard
streamlit run dashboard.py
```
Dengan menjalankan perintah di atas, dashboard akan terbuka di browser web Anda secara lokal.

## Cara menjalankan Streamlit dengan Localhost server anda
1. Unduh dataset yang tertera di atas dengan format .csv.
2. Jalankan kode (dashboard.py) ke dalam EDA (Exploratory Data Analysis) kesukaan Anda.
3. Instal Streamlit pada command prompt Anda dengan menjalankan:
```
pip install streamlit
```
4. Setelah instalasi selesai, navigasikan ke folder dashboard/ dan buka file (dashboard.py) dengan perintah berikut:
```
cd dashboard
streamlit run dashboard.py
```
5. Dashboard akan terlihat di browser web Anda secara lokal.

## hal yang di tampil Dashboard pada streamlit.io
Dashboard Streamlit mencakup fitur-fitur berikut:

1. Tampilan interaktif dari data mentah dan statistik ringkasan.
2. Visualisasi yang menjawab pertanyaan bisnis kunci:
-  Apakah terdapat sebuah pola tren yang dapat disimpulkan? jika benar adanya pola, bagaimana polanya serta pada tahun berapa serta pada bulan apa jumlah pengguna berapa pada titik tertingginya?
- Dari analisis, terlihat bahwa jumlah pengguna sepeda menunjukkan tren kenaikan yang konsisten dari bulan Januari hingga Juni, dengan bulan Juni mencatat jumlah tertinggi. Apakah peningkatan jumlah pengguna pada bulan-bulan yang lebih hangat (April, Mei, dan Juni) mencerminkan pengaruh cuaca baik terhadap minat masyarakat untuk bersepeda?
  
## Kebutuhan dan Instalasi
Proyek ini memerlukan pustaka-pustaka berikut untuk berjalan dengan baik:
- Matplotlib 3.8.3
- NumPy 1.26.4
- Pandas 2.2.0
- Seaborn 0.13.2
- Streamlit 1.31.1
