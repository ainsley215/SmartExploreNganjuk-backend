import pandas as pd

from math import radians
from math import sin
from math import cos
from math import sqrt
from math import atan2


def haversine(
    lat1,
    lon1,
    lat2,
    lon2
):

    R = 6371

    lat1 = radians(lat1)
    lon1 = radians(lon1)

    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        sin(dlat / 2) ** 2
        +
        cos(lat1)
        *
        cos(lat2)
        *
        sin(dlon / 2) ** 2
    )

    c = 2 * atan2(
        sqrt(a),
        sqrt(1 - a)
    )

    return R * c


def optimasi_rute(
    df_rekomendasi,
    start_lat,
    start_lon
):

    wisata = df_rekomendasi.copy()

    route = []

    current_lat = start_lat
    current_lon = start_lon

    while len(wisata) > 0:

        nearest_index = None

        nearest_distance = float(
            "inf"
        )

        for idx, row in wisata.iterrows():

            distance = haversine(
                current_lat,
                current_lon,
                row["latitude"],
                row["longitude"]
            )

            if distance < nearest_distance:

                nearest_distance = distance

                nearest_index = idx

        current = wisata.loc[
            nearest_index
        ]

        route.append(current)

        current_lat = current[
            "latitude"
        ]

        current_lon = current[
            "longitude"
        ]

        wisata = wisata.drop(
            nearest_index
        )

    return pd.DataFrame(
        route
    ).reset_index(
        drop=True
    )