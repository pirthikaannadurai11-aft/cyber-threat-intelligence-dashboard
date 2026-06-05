from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/alerts')
def alerts():
    return jsonify([
        {"msg": "Virus detected in file.exe"},
        {"msg": "Suspicious login attempt from unknown IP"},
        {"msg": "Malware signature detected"},
        {"msg": "Unusual data access pattern found"}
    ])

@app.route('/stats')
def stats():
    return jsonify({
        "safe_files": 15,
        "threat_files": 3
    })

if __name__ == "__main__":
    app.run(debug=True)