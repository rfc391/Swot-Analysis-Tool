from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId
from swot_ai_helper import SWOTAIHelper
import datetime
from flask_cors import CORS # Added import for CORS

app = Flask(__name__)
CORS(app) # Enable CORS
client = MongoClient("mongodb://0.0.0.0:27017/")
db = client['swot_analysis_db']
collection = db['swot_entries']

# AI Helper
ai_helper = SWOTAIHelper()

@app.route('/api/swot', methods=['POST'])
def create_swot():
    data = request.json
    entry = {
        "strengths": data.get("strengths", []),
        "weaknesses": data.get("weaknesses", []),
        "opportunities": data.get("opportunities", []),
        "threats": data.get("threats", []),
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow(),
    }
    result = collection.insert_one(entry)
    return jsonify({"id": str(result.inserted_id)}), 201

@app.route('/api/swot/suggest', methods=['POST'])
def suggest_swot():
    data = request.json
    category = data.get("category")
    description = data.get("description")
    if not category or not description:
        return jsonify({"error": "Both 'category' and 'description' are required."}), 400
    suggestions = ai_helper.suggest_swot(category, description)
    return jsonify({"suggestions": suggestions})

@app.route('/api/swot', methods=['GET'])
def get_all_swots():
    entries = collection.find()
    return jsonify([
        {
            "id": str(entry["_id"]),
            "strengths": entry["strengths"],
            "weaknesses": entry["weaknesses"],
            "opportunities": entry["opportunities"],
            "threats": entry["threats"],
            "created_at": entry["created_at"],
            "updated_at": entry["updated_at"],
        }
        for entry in entries
    ])

if __name__ == "__main__":
    app.run(debug=True)