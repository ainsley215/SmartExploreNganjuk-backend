import os
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

CSV_PATH = os.path.join(
    BASE_DIR,
    "data",
    "dataset_wisataa.csv"
)

df = pd.read_csv(CSV_PATH)

df["kategori"] = df["kategori"].fillna("")
df["deskripsi"] = df["deskripsi"].fillna("")
df["tags"] = df["tags"].fillna("")

df["fitur"] = (
    df["kategori"] + " " +
    df["tags"] + " " +
    df["deskripsi"]
)

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(
    df["fitur"]
)


def rekomendasi_wisata(
    preferensi,
    top_n=5
):

    is_rating = False

    try:
        target_rating = float(preferensi)
        is_rating = True

    except ValueError:
        is_rating = False

    if is_rating:

        hasil = df[
            df["rating"] == target_rating
        ].copy()

        if hasil.empty:

            hasil = df[
                df["rating"] >= target_rating
            ].copy()

        hasil["similarity"] = 1.0
        hasil["rating_norm"] = (
            hasil["rating"] / 5
        )

        hasil["final_score"] = (
            hasil["rating_norm"]
        )

        hasil = hasil.sort_values(
            by="rating",
            ascending=False
        )

    else:

        query_vector = vectorizer.transform(
            [preferensi]
        )

        similarity_scores = cosine_similarity(
            query_vector,
            tfidf_matrix
        ).flatten()

        hasil = df.copy()

        hasil["similarity"] = similarity_scores

        hasil["rating_norm"] = (
            hasil["rating"] / 5
        )

        hasil["final_score"] = (
            0.8 * hasil["similarity"]
            +
            0.2 * hasil["rating_norm"]
        )

        hasil = hasil.sort_values(
            by="final_score",
            ascending=False
        )

    return hasil[
        [
            "nama",
            "kategori",
            "rating",
            "latitude",
            "longitude",
            "similarity",
            "final_score"
        ]
    ].head(top_n)