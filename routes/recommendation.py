from flask import Blueprint, jsonify, request

from services.recommendation_service import (
    get_recommendation
)

recommend_bp = Blueprint(
    "recommend",
    __name__
)

@recommend_bp.route(
    "/recommend",
    methods=["POST"]
)
def recommend():

    data = request.get_json(silent=True)

    # Validasi
    if not data:
        return jsonify({
            "error": "Body JSON tidak boleh kosong"
        }), 400

    if "kategori" not in data:
        return jsonify({
            "error": "kategori wajib diisi"
        }), 400

    kategori = data["kategori"]

    hasil = get_recommendation(
        kategori
    )

    return jsonify(hasil)