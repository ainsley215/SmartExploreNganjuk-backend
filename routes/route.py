from flask import Blueprint
from flask import request
from flask import jsonify

from services.route_service import (
    get_route
)

route_bp = Blueprint(
    "route",
    __name__
)

@route_bp.route(
    "/route",
    methods=["POST"]
)
def route():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Body JSON tidak boleh kosong"
        }), 400

    kategori = data.get(
        "kategori"
    )

    latitude = data.get(
        "latitude"
    )

    longitude = data.get(
        "longitude"
    )

    hasil = get_route(
        kategori,
        latitude,
        longitude
    )

    return jsonify({
        "status": "success",
        "data": hasil
    })