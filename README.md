# Backend Wisata Nganjuk

## Menjalankan Project

Install dependency:

```bash
pip install flask pandas scikit-learn
```

Jalankan aplikasi:

```bash
py app.py
```

Server berjalan pada:

```text
http://127.0.0.1:5000
```

---

## Endpoint

### 1. GET /destinations

Mengambil seluruh data destinasi wisata.

#### Request

```http
GET /destinations
```

---

### 2. GET /destinations/<id>

Mengambil detail destinasi berdasarkan ID.

#### Request

```http
GET /destinations/1
```

---

### 3. POST /recommend

Menghasilkan rekomendasi wisata berdasarkan kategori yang dipilih pengguna.

#### Request

```http
POST /recommend
```

#### Body

```json
{
    "kategori": "Alam"
}
```

---

### 4. POST /route

Menghasilkan rute wisata terbaik berdasarkan kategori dan lokasi pengguna.

#### Request

```http
POST /route
```

#### Body

```json
{
    "kategori": "Alam",
    "latitude": -7.5498074,
    "longitude": 111.8347322
}
```

---

## Teknologi yang Digunakan

* Python
* Flask
* Pandas
* Scikit-Learn
* TF-IDF Vectorizer
* Cosine Similarity

---

## Fitur

* Menampilkan seluruh destinasi wisata
* Menampilkan detail destinasi wisata
* Rekomendasi wisata berbasis AI
* Optimasi rute wisata berdasarkan lokasi pengguna

---
ML
https://drive.google.com/file/d/1Vq7O2JlXJkFadOS-yFwUn9jMzfBkdbpG/view?usp=sharing
