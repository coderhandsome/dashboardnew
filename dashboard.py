import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Muat dataset
day_data = pd.read_csv("D:/submission/dashboard/day_data.csv")  # Ganti dengan path dataset harian
hour_data = pd.read_csv("D:/submission/dashboard/hour_data.csv")  # Ganti dengan path dataset per jam
# Ubah kolom tanggal menjadi datetime
day_data["dteday"] = pd.to_datetime(day_data["dteday"])
# Buat Sidebar filter
st.sidebar.header("Filter Data")
selected_year = st.sidebar.selectbox("Pilih Tahun:", sorted(day_data["yr"].unique()))
# Nama hari
hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
day_data["weekday"] = day_data["weekday"].apply(lambda x: hari[x])
# ----- DASHBOARD -----
st.title("Dashboard Penyewaan Sepeda")
# ---- VISUALISASI 1: Rata-rata Penyewaan per Hari ----
st.subheader("Rata-rata Penyewaan Perhari")
weekday_avg = day_data.groupby("weekday")["cnt"].mean().reset_index()
colors = ["#89CFF0" if day != "Jumat" else "#0057B7" for day in weekday_avg["weekday"]]

fig, ax = plt.subplots()
sns.barplot(x="weekday", y="cnt", data=weekday_avg, palette=colors, ax=ax)
ax.set_xlabel("Hari")
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_title("Rata-rata Penyewaan Sepeda per Hari dalam Seminggu")
plt.xticks(rotation=45)
st.pyplot(fig)
# ---- VISUALISASI 2: Rata-rata Penyewaan per Jam ----
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Jam")
hour_avg = hour_data.groupby("hr")["cnt"].mean().reset_index()
fig, ax = plt.subplots()
sns.lineplot(x="hr", y="cnt", data=hour_avg, marker="o", ax=ax)
ax.set_xlabel("Jam dalam Sehari")
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_title("Rata-rata Penyewaan Sepeda per Jam")
st.pyplot(fig)
# ---- VISUALISASI 3: Tren Penyewaan Sepeda Bulanan ----
st.subheader("Penyewaan Sepeda Bulanan")
monthly_trend = day_data.groupby(["yr", "mnth"])["cnt"].sum().reset_index()
fig, ax = plt.subplots()
sns.lineplot(x="mnth", y="cnt", hue="yr", data=monthly_trend, marker="o", ax=ax, palette=["#1f77b4", "#ff7f0e"])
ax.set_xticks(range(1, 13))
ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"])
ax.set_xlabel("Bulan")
ax.set_ylabel("Total Penyewaan")
ax.set_title("Tren Penyewaan Sepeda Bulanan (Dibedakan Berdasarkan Tahun)")
st.pyplot(fig)

# ---- Kesimpulan ----
st.subheader("Kesimpulan")
st.markdown("""
- Conclution pertanyaan 1: Kapan jumlah penyewaan sepeda mencapai tingkat tertinggi dan terendah?
    - Peminjaman tahun 2012 lebih tinggi dibandingkan tahun 2011
    - Mei-Agustus memiliki penyewaan tertinggi dan Desember-Februari memiliki penyewaan terendah.
- Conclution pertanyaan 2: Bagaimana variasi jumlah penyewaan sepeda pada setiap hari dalam seminggu?
    - Hari kerja (senin sampai jum'at) cenderung memiliki jumlah penyewaan lebih tinggi dibandingkan akhir peka.
    - Sabtu & minggu memiliki penyewaan lebih rendah
    - Penyewaan terbanyak biasanya terjadi pada hari kerja
- Conclution pertanyaan 3: Pada jam berapa dalam sehari jumlah penyewaan sepeda paling tinggi dan paling rendah?
    - Dua puncak penyewaan pada pagi hari (07.00-09.00) dan sore hari (17.00-19.00)
    - Penyewaan paling sedikit terhadi pada pukul 00.00-05.00.
    - Setelah pukul 21.00 penyewaan menurun drastis.
""")
