
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from swot_analysis import SWOTAnalysis
from swot_ai_helper import SWOTAIHelper
import json

app = Flask(__name__)
CORS(app)

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

# Setup MongoDB connection
client = MongoClient(config['database_url'])
db = client.swot_database
swot_handler = SWOTAnalysis(db)
ai_helper = SWOTAIHelper()

@app.route('/api/swot', methods=['POST'])
def create_swot():
    data = request.get_json()
    analysis_id = swot_handler.create_analysis(
        data.get('strengths', []),
        data.get('weaknesses', []),
        data.get('opportunities', []),
        data.get('threats', [])
    )
    return jsonify({"id": str(analysis_id)}), 201

@app.route('/api/swot/<analysis_id>', methods=['GET'])
def get_swot(analysis_id):
    analysis = swot_handler.get_analysis(analysis_id)
    if analysis:
        analysis['_id'] = str(analysis['_id'])
        return jsonify(analysis)
    return jsonify({"error": "Not found"}), 404

@app.route('/api/swot/suggest', methods=['POST'])
def get_suggestions():
    data = request.get_json()
    suggestions = ai_helper.suggest_swot(
        data.get('category'),
        data.get('description')
    )
    return jsonify({"suggestions": suggestions})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
