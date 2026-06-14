from ai.recommendation_model import (
    rekomendasi_wisata
)


def get_recommendation(
    kategori
):

    hasil = rekomendasi_wisata(
        kategori
    )

    return hasil.to_dict(
        orient="records"
    )