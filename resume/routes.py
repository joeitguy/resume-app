from flask import Blueprint, jsonify
import os, json

resume_bp = Blueprint('resume', __name__, url_prefix='/api/resume')

@resume_bp.route('/meta', methods=['GET'])
def get_resume_meta():
    try:
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resume_meta.json'))
        with open(path, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "resume_meta.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 500