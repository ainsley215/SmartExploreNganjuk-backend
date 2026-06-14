# import os
# import pandas as pd
# from flask import Blueprint, jsonify

# destinations_bp = Blueprint(
#     "destinations",
#     __name__
# )

# BASE_DIR = os.path.dirname(
#     os.path.dirname(os.path.abspath(__file__))
# )

# CSV_PATH = os.path.join(
#     BASE_DIR,
#     "data",
#     "dataset_wisataa.csv"
# )

# @destinations_bp.route("/destinations")
# def get_destinations():
#     # Membaca CSV
#     df = pd.read_csv(CSV_PATH)
    
#     df = df.where(pd.notnull(df), None)
    
#     if 'id' in df.columns:
#         df['id'] = df['id'].fillna(0).astype(int)
#     # -----------------------------------------------------------

#     return jsonify(df.to_dict("records"))

# @destinations_bp.route("/destinations/<int:id>")
# def get_destination(id):
#     df = pd.read_csv(CSV_PATH)
    
#     # Pastikan id yang dicari juga dibersihkan
#     df['id'] = df['id'].fillna(0).astype(int)
    
#     result = df[df["id"] == id]

#     if result.empty:
#         return jsonify({
#             "error": "Destinasi tidak ditemukan"
#         }), 404

#     return jsonify(
#         result.to_dict("records")[0]
#     )

# @destinations_bp.route("/destinations/<identifier>", methods=["GET"])
# def get_destination_by_identifier(identifier): # Nama fungsi dibuat unik
#     df = pd.read_csv(CSV_PATH)
#     nama_wisata = identifier.replace('%20', ' ')
    
#     # Logika pencarian
#     if identifier.isdigit():
#         result = df[df["id"] == int(identifier)]
#     else:
#         result = df[df["nama"].str.lower() == nama_wisata.lower()]
        
#     if result.empty:
#         return jsonify({"error": "Destinasi tidak ditemukan"}), 404
#     return jsonify(result.to_dict("records")[0])

import os
import pandas as pd
from flask import Blueprint, jsonify

destinations_bp = Blueprint("destinations", __name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "data", "dataset_wisataa.csv")

# Helper untuk load data
def get_df():
    return pd.read_csv(CSV_PATH)

@destinations_bp.route("/destinations", methods=["GET"])
def get_destinations():
    df = get_df()
    df = df.where(pd.notnull(df), None)
    return jsonify(df.to_dict("records"))

@destinations_bp.route("/destinations/<identifier>", methods=["GET"])
def get_detail(identifier):
    df = get_df()
    search_term = identifier.lower().strip()
    
    # Cari berdasarkan ID (jika angka) atau Nama
    if search_term.isdigit():
        data_detail = df[df['id'].astype(str) == search_term]
    else:
        data_detail = df[df['nama'].astype(str).str.lower() == search_term]
        
    if not data_detail.empty:
        return jsonify(data_detail.iloc[0].to_dict()), 200
    else:
        return jsonify({"error": "Destinasi tidak ditemukan"}), 404
    

print(f"DEBUG: Mencari CSV di: {CSV_PATH}")
if not os.path.exists(CSV_PATH):
    print("!!! ERROR: FILE CSV TIDAK DITEMUKAN DI PATH TERSEBUT !!!")
else:
    print("--- SUCCESS: FILE CSV DITEMUKAN ---")

