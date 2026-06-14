from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.destinations import destinations_bp
from ai.recommendation_model import rekomendasi_wisata
from ai.route_optimizer import optimasi_rute


app = Flask(__name__)
CORS(app) # Mengizinkan semua akses

# Daftarkan Blueprint
app.register_blueprint(destinations_bp)

# Rute Update Profile
@app.route('/profile/update', methods=['POST'])
def update_profile():
    data = request.get_json()
    print("Data diterima:", data)
    return jsonify({"status": "sukses"}), 200

# 2. Rute API Rekomendasi AI TF-IDF (Pindahkan ke atas app.run)
@app.route('/api/rekomendasi', methods=['GET'])
def get_rekomendasi():
    query = request.args.get('q', '')

    lat = request.args.get('lat', type=float)
    lon = request.args.get('lon', type=float)
    
    if not query or query == "Semua":
        # Jika memilih 'Semua', panggil fungsi AI dengan string kosong
        hasil_df = rekomendasi_wisata(preferensi="", top_n=20)
    else:
        # Masukkan kata kunci ke mesin AI TF-IDF
        hasil_df = rekomendasi_wisata(preferensi=query, top_n=10)
        
    if lat is not None and lon is not None:
        hasil_df = optimasi_rute(hasil_df, lat, lon)

    # Ubah DataFrame hasil rekomendasi menjadi JSON
    data_json = hasil_df.to_dict(orient='records')
    return jsonify(data_json)

# 3. PASTIKAN BLOCK INI BERADA DI PALING BAWAH FILE
if __name__ == '__main__':
    app.run(debug=True, port=5000)


@destinations_bp.route('/destinations/<identifier>', methods=['GET'])
def get_detail(identifier):
    search_term = identifier.lower().strip()
    data_detail = df[df['nama'].astype(str).str.lower() == search_term]
    if data_detail.empty:
        data_detail = df[df['id'].astype(str) == search_term]
    if not data_detail.empty:
        result = data_detail.iloc[0].to_dict()
        return jsonify(result), 200
    else:
        return jsonify({"error": "Destinasi tidak ditemukan"}), 404