
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from swot_analysis import SWOTAnalysis
from swot_ai_helper import SWOTAIHelper
import json
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)
CORS(app)

def init_app():
    # Load configuration
    try:
        with open('config.json') as config_file:
            config = json.load(config_file)
    except Exception as e:
        logging.error(f"Failed to load config: {e}")
        raise

    # Setup MongoDB connection
    try:
        client = MongoClient(config['database_url'])
        db = client.swot_database
        return SWOTAnalysis(db), SWOTAIHelper()
    except Exception as e:
        logging.error(f"Failed to connect to database: {e}")
        raise

swot_handler, ai_helper = init_app()

@app.route('/api/swot', methods=['POST'])
def create_swot():
    try:
        data = request.get_json()
        analysis_id = swot_handler.create_analysis(
            data.get('strengths', []),
            data.get('weaknesses', []),
            data.get('opportunities', []),
            data.get('threats', [])
        )
        return jsonify({"id": str(analysis_id)}), 201
    except Exception as e:
        logging.error(f"Error creating SWOT analysis: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/swot/<analysis_id>', methods=['GET'])
def get_swot(analysis_id):
    try:
        analysis = swot_handler.get_analysis(analysis_id)
        if analysis:
            analysis['_id'] = str(analysis['_id'])
            return jsonify(analysis)
        return jsonify({"error": "Not found"}), 404
    except Exception as e:
        logging.error(f"Error retrieving SWOT analysis: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/swot/suggest', methods=['POST'])
def get_suggestions():
    try:
        data = request.get_json()
        if not data.get('category') or not data.get('description'):
            return jsonify({"error": "Category and description are required"}), 400
            
        suggestions = ai_helper.suggest_swot(
            data['category'],
            data['description']
        )
        return jsonify({"suggestions": suggestions})
    except Exception as e:
        logging.error(f"Error getting suggestions: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
