from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/run_model", methods=["POST", "GET"])
def run_model():
    # For now, just return a dummy response
    return jsonify({"message": "LLaMA model response!"})

if __name__ == "__main__":
    print("✅ LLaMA service container is running!")
    # Bind to 0.0.0.0 so other containers can reach it
    app.run(host="0.0.0.0", port=5000)
