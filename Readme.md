# Proyek Analisis Data Bike Sharing

## Deskripsi
Proyek ini menganalisis data penyewaan sepeda dari Capital Bikeshare Washington D.C. (2011-2012) untuk menjawab:
1. Bagaimana pengaruh kondisi cuaca terhadap total penyewaan?
2. Bagaimana perbandingan pola penyewaan antara pengguna casual dan registered berdasarkan musim dan tahun?

## Struktur Folder
- `notebook.ipynb` : Analisis lengkap (EDA, visualisasi, binning)
- `dashboard/` : Dashboard Streamlit
  - `main_data.csv` : Data olahan (hasil dari notebook)
  - `dashboard.py` : Script dashboard
- `data/` : Dataset asli (day.csv, hour.csv)
- `requirements.txt` : Daftar library
- `url.txt` : Link deployment Streamlit

## Cara Menjalankan
1. Install dependencies: `pip install -r requirements.txt`
2. Jalankan notebook untuk menghasilkan `main_data.csv` (opsional, sudah disediakan)
3. Jalankan dashboard: `streamlit run dashboard/dashboard.py`

## Hasil Analisis
- Cuaca buruk menurunkan penyewaan hingga >50%.
- Pengguna registered lebih stabil sepanjang tahun, casual melonjak di musim panas.
- Clustering binning mengelompokkan hari menjadi Low/Medium/High demand untuk rekomendasi operasional.