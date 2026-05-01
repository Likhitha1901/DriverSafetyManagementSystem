from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Driver Safety Server Running"

@app.route("/data")
def data():
    return jsonify({
        "status": "Server Running",
        "alerts": []
    })

@app.route("/update", methods=["POST"])
def update():
    data = request.json
    return jsonify({
        "message": "Update received",
        "received": data
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)