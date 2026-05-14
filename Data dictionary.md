# Data Dictionary — AUVRA AI-UV Repair & Analysis

## Deskripsi Dataset

Dataset ini digunakan untuk pengembangan sistem Artificial Intelligence berbasis Computer Vision dalam mendeteksi dan mengklasifikasikan tingkat keparahan gangguan kulit akibat paparan UV dan berbagai kondisi kulit lainnya.

Dataset terdiri dari gambar kulit yang telah dikelompokkan berdasarkan:

- Tingkat keparahan (severity)
- Jenis penyakit kulit (disease)

Dataset telah melalui proses:

- Data Wrangling
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Image Preprocessing
- Dataset Splitting

Sehingga siap digunakan oleh tim AI untuk proses training model Deep Learning.

---

# Struktur Dataset

```text
clean_data/
│
├── train/
├── val/
└── test/
```

Struktur setiap split:

```text
train/
   ├── Normal/
   │    ├── Disease_Name/
   │    │     ├── image1.jpg
   │    │     └── ...
   │
   ├── Ringan/
   ├── Sedang/
   └── Terparah/
```

---

# Data Dictionary

| Kolom | Tipe Data | Deskripsi |
|---|---|---|
| severity | string | Tingkat keparahan kondisi kulit seperti Normal, Ringan, Sedang, dan Terparah. |
| disease | string | Nama penyakit atau kondisi kulit pada gambar. |
| filename | string | Nama file gambar. |
| filepath | string | Lokasi/path file gambar pada dataset. |
| width | integer | Lebar gambar dalam pixel sebelum preprocessing. |
| height | integer | Tinggi gambar dalam pixel sebelum preprocessing. |
| format | string | Format gambar seperti JPG, JPEG, PNG, atau WEBP. |
| mode | string | Mode warna gambar seperti RGB atau grayscale. |
| split_type | string | Jenis split dataset: train, validation, atau test. |

---

# Deskripsi Severity

| Severity | Deskripsi |
|---|---|
| Normal | Kulit dalam kondisi normal tanpa indikasi gangguan serius. |
| Ringan | Gangguan kulit ringan dengan gejala awal atau lokal. |
| Sedang | Gangguan kulit tingkat menengah dengan area yang lebih terlihat. |
| Terparah | Gangguan kulit berat dengan kondisi yang signifikan. |

---

# Standarisasi Preprocessing

| Proses | Keterangan |
|---|---|
| Resize | Semua gambar diubah menjadi ukuran 224x224 pixel |
| RGB Conversion | Semua gambar dikonversi menjadi RGB |
| Duplicate Removal | Menghapus gambar duplikat |
| Corrupt Checking | Menghapus gambar rusak atau tidak terbaca |
| Dataset Split | Dataset dibagi menjadi train, validation, dan test |

---

# Tujuan Dataset

Dataset digunakan untuk:

- Klasifikasi tingkat keparahan penyakit kulit
- Analisis kondisi kulit berbasis AI
- Pelatihan model Deep Learning Computer Vision
- Pengembangan sistem diagnosis awal berbasis citra kulit
- Deployment aplikasi AI berbasis web/mobile

---

# Teknologi yang Digunakan

| Kebutuhan | Tools |
|---|---|
| Data Wrangling | pandas |
| Image Processing | Pillow, OpenCV |
| Visualisasi | matplotlib, seaborn |
| AI Model | TensorFlow / PyTorch |
| Dashboard | Streamlit |

---

# Catatan

- Dataset ini digunakan hanya untuk tujuan edukasi dan pengembangan sistem AI.
- Hasil prediksi model tidak menggantikan diagnosis medis profesional.
- Seluruh gambar telah melalui proses preprocessing sebelum digunakan pada model AI.
