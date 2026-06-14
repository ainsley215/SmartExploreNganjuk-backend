from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.destinations import destinations_bp
from ai.recommendation_model import rekomendasi_wisata
from ai.route_optimizer import optimasi_rute
import os

app = Flask(__name__)
CORS(app, origins=["https://smart-explore-nganjuk-frontend-pera-eta.vercel.app"])

# Daftarkan Blueprint SEKALI SAJA
app.register_blueprint(destinations_bp)

@app.route('/profile/update', methods=['POST'])
def update_profile():
    data = request.get_json()
    return jsonify({"status": "sukses"}), 200

@app.route('/api/rekomendasi', methods=['GET'])
def get_rekomendasi():
    query = request.args.get('q', '')
    lat = request.args.get('lat', type=float)
    lon = request.args.get('lon', type=float)
    
    if not query or query == "Semua":
        hasil_df = rekomendasi_wisata(preferensi="", top_n=20)
    else:
        hasil_df = rekomendasi_wisata(preferensi=query, top_n=10)
        
    if lat is not None and lon is not None:
        hasil_df = optimasi_rute(hasil_df, lat, lon)

    return jsonify(hasil_df.to_dict(orient='records'))

@app.route('/')
def hello():
    return "Aplikasi Berhasil Jalan!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Backend SmartExplore Nganjuk Aktif!"}), 200

@app.before_request
def log_request_info():
    print(f"DEBUG: Menerima request ke: {request.url}")