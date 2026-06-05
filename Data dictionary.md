# Data Dictionary — AUVRA AI-UV Repair & Analysis


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

# Catatan

- Dataset ini digunakan hanya untuk tujuan edukasi dan pengembangan sistem AI.
- Hasil prediksi model tidak menggantikan diagnosis medis profesional.

