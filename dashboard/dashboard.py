import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set title
st.title('Bike Sharing Dashboard')
st.markdown('Analisis penyewaan sepeda berdasarkan cuaca, musim, dan tipe pengguna.')

# Load data
import os
# Gunakan path relatif terhadap file dashboard.py
current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, 'main_data.csv')
df = pd.read_csv(csv_path)

# Sidebar filters
st.sidebar.header('Filter Data')
selected_year = st.sidebar.selectbox('Pilih Tahun', options=sorted(df['yr'].unique()), format_func=lambda x: '2011' if x==0 else '2012')
selected_weather = st.sidebar.multiselect('Pilih Kondisi Cuaca', options=sorted(df['weathersit'].unique()), default=sorted(df['weathersit'].unique()), format_func=lambda x: {1:'Cerah',2:'Berkabut',3:'Hujan Ringan',4:'Hujan Berat'}[x])

# Filter dataframe
filtered_df = df[(df['yr'] == selected_year) & (df['weathersit'].isin(selected_weather))].copy()

# Pertanyaan 1: Hubungan Cuaca dengan Penyewaan
st.subheader('Pengaruh Kondisi Cuaca terhadap Total Penyewaan')
fig1, ax1 = plt.subplots(figsize=(8,5))
sns.barplot(data=filtered_df, x='weathersit', y='cnt', ci=None, palette='Blues_d', ax=ax1)
ax1.set_xlabel('Kondisi Cuaca (1=Cerah, 2=Berkabut, 3=Hujan Ringan, 4=Hujan Berat)')
ax1.set_ylabel('Rata-rata Total Penyewaan')
ax1.set_title(f'Tahun {2011 if selected_year==0 else 2012}')
st.pyplot(fig1)

# Pertanyaan 2: Perbandingan Penyewa Casual vs Registered per Musim dan Tahun
st.subheader('Perbandingan Casual vs Registered per Musim')
season_map = {1:'Spring', 2:'Summer', 3:'Fall', 4:'Winter'}
filtered_df['season_name'] = filtered_df['season'].map(season_map)
season_group = filtered_df.groupby('season_name')[['casual', 'registered']].mean().reset_index()

fig2, ax2 = plt.subplots(figsize=(10,5))
x = range(len(season_group))
width = 0.35
ax2.bar([i - width/2 for i in x], season_group['casual'], width, label='Casual')
ax2.bar([i + width/2 for i in x], season_group['registered'], width, label='Registered')
ax2.set_xticks(x)
ax2.set_xticklabels(season_group['season_name'])
ax2.set_ylabel('Rata-rata Jumlah Penyewaan')
ax2.set_title(f'Tahun {2011 if selected_year==0 else 2012}')
ax2.legend()
st.pyplot(fig2)

# --- Analisis Lanjutan: Tingkat Penyewaan (Binning) ---
st.subheader('Distribusi Tingkat Penyewaan (Low, Medium, High)')
level_counts = filtered_df['rental_level'].value_counts()
fig3, ax3 = plt.subplots()
ax3.pie(level_counts, labels=level_counts.index, autopct='%1.1f%%', startangle=90)
ax3.axis('equal')
st.pyplot(fig3)

st.caption('Sumber data: Capital Bikeshare, Washington D.C. (2011-2012)')
