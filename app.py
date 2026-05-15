import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import os

# =========================
# ===== CONFIG =====
st.set_page_config(page_title="AUVRA", page_icon="🔥", layout="wide")

# ===== SESSION LOGIN =====
if "login" not in st.session_state:
    st.session_state.login = False 

# ===== LOGIN PAGE =====
if not st.session_state.login:
    st.markdown("<h1 style='text-align:center;'>🔥 AUVRA : AI-UV Repair & Analysis Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Silahkan masukkan nama anda.</h3>", unsafe_allow_html=True)

    name = st.text_input("Nama Anda")

    if st.button("Login"):
        if name != "":
            st.session_state.login = True
            st.session_state.user = name
            st.rerun()
        else:
            st.warning("Mohon isi nama Anda terlebih dahulu!")

    st.stop()

# ===== STYLE =====
st.markdown("""
<style>
.main {
    background-color: #0E1117;
    color: white;
}
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("metadata_raw_dataset.csv")

# ===== SIDEBAR =====
st.sidebar.title(f"👋 Halo, {st.session_state.user}")

menu_list = [
    "🏠 Home",
    "📊 Jenis Kerusakan Kulit",
    "🔥 Tingkat Keparahan",
    "📂 Preview Metadata Dataset"
]

# default menu
if "menu" not in st.session_state:
    st.session_state.menu = "🏠 Home"

st.sidebar.title("📂 Menu")

for item in menu_list:
    if st.sidebar.button(item, use_container_width=True):
        st.session_state.menu = item

menu = st.session_state.menu

st.markdown("""
<style>
div.stButton > button {
    text-align: left;
    padding: 12px 20px;
    margin-bottom: 5px;
    border-radius: 12px;
    background-color: #1f2937;
    color: gold;
    border: none;
    font-size: 20px;
}
div.stButton > button:hover {
    background-color: #374151;
    transform: translateX(7px);
}
</style>
""", unsafe_allow_html=True)
# =========================
# HOME
# =========================
if menu == "🏠 Home":

    st.title("AUVRA - AI-UV Repair & Analysis")

    st.markdown("""
    Dashboard ini digunakan untuk analisis dataset kerusakan kulit 
    berdasarkan tingkat severity menggunakan image processing.
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Jumlah Dataset", len(df))
    col2.metric("Jumlah Kategori", 4)
    col3.metric("Jumlah Metadata", len(df.columns))

    st.image("home.jpeg", use_container_width=True)

    st.subheader("Kategori Tingkat Keparahan")

    col4, col5, col6, col7 = st.columns(4)

    col4.metric("✅ Normal", 872)
    col5.metric("Ringan", 2894)
    col6.metric("Sedang", 2029)
    col7.metric("Terparah", 8307)

    st.info(
        "AUVRA membantu proses identifikasi kondisi kulit menggunakan pendekatan visual dan machine learning."
    )

# =========================
# DISTRIBUSI DATASET
# =========================
elif menu == "📊 Jenis Kerusakan Kulit":

    st.title("📊 Jenis Kerusakan Kulit yang Paling Dominan")

    penyakit = []
    jumlah_data = []
    df = pd.read_csv("metadata_raw_dataset.csv")

    penyakit_df = df["disease"].value_counts().reset_index()

    penyakit_df.columns = ["Penyakit", "Jumlah Data"]

    fig = px.bar(
        penyakit_df,
        x="Penyakit",
        y="Jumlah Data",
        color="Jumlah Data",
        text="Jumlah Data",
        title="Distribusi Dataset Berdasarkan Jenis Kerusakan Kulit"
    )

    fig.update_layout(
        xaxis_title="Jenis Kerusakan Kulit",
        yaxis_title="Jumlah Data",
        xaxis_tickangle=-45
    )

    st.plotly_chart(fig, use_container_width=True)

    st.write("""
    Grafik menunjukkan jumlah gambar pada setiap jenis penyakit kulit dalam dataset.
    Distribusi data membantu memahami keseimbangan dataset sebelum proses training machine learning.
    """)

# =========================
# SEVERITY ANALYSIS
# =========================
elif menu == "🔥 Tingkat Keparahan":

    st.title("🔥 Tingkat Keparahan")

    severity_df = df["severity"].value_counts().reset_index()

    severity_df.columns = ["Severity", "Jumlah Data"]

    fig = px.pie(
        severity_df,
        names="Severity",
        values="Jumlah Data",
        title="Persentase Tingkat Severity Kerusakan Kulit"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.write("""
    Visualisasi menunjukkan proporsi jumlah gambar pada setiap tingkat severity kerusakan kulit.
    Data dihitung dari seluruh gambar di dalam setiap kategori severity beserta subfolder penyakitnya.
    """)

# =========================
# DATASET PREVIEW
# =========================
elif menu == "📂 Preview Metadata Dataset":

    st.title("📂 Preview Metadata Dataset")

    st.dataframe(df.head(20))

    st.write("""
    Tabel di atas merupakan preview metadata dataset yang digunakan 
    dalam proses analisis dan training model.
    """)
