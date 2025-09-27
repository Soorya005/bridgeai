from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

LLAMA_URL = "http://llama-service:5000/run_model"

@app.route("/ask", methods=["GET"])
def ask():
    query = request.args.get("query", "")
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    try:
        resp = requests.get(LLAMA_URL)
        return jsonify({"query": query, "llama_response": resp.json()})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Ensure Flask listens on all interfaces inside the container
    app.run(host="0.0.0.0", port=8000, debug=True)
