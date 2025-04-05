
from flask import Flask, jsonify, request
from core import FileHandler

app = Flask(__name__)

@app.route("/copy", methods=["POST"])
def copy_file():
    data = request.get_json()
    src = data.get("src")
    dst = data.get("dst")
    response = FileHandler.copy_file(src, dst)
    return jsonify({"message": response})

@app.route("/move", methods=["POST"])
def move_file():
    data = request.get_json()
    src = data.get("src")
    dst = data.get("dst")
    response = FileHandler.move_file(src, dst)
    return jsonify({"message": response})

@app.route("/delete", methods=["POST"])
def delete_file():
    data = request.get_json()
    filepath = data.get("filepath")
    response = FileHandler.delete_file(filepath)
    return jsonify({"message": response})

if __name__ == "__main__":
    app.run(debug=True)
