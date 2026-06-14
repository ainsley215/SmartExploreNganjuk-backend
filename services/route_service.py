from ai.recommendation_model import (
    rekomendasi_wisata
)

from ai.route_optimizer import (
    optimasi_rute
)

def get_route(
    kategori,
    latitude,
    longitude
):

    hasil = rekomendasi_wisata(
        kategori
    )

    rute = optimasi_rute(
        hasil,
        latitude,
        longitude
    )

    return rute.to_dict(
        orient="records"
    )