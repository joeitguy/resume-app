import os
import json
from flask import Blueprint, jsonify

resume_bp = Blueprint('resume', __name__, url_prefix='/api/resume')

@resume_bp.route('/meta', methods=['GET'])
def get_resume_meta():
    path = os.path.join(os.path.dirname(__file__), '..', 'resume_meta.json')
    path = os.path.abspath(path)

    if not os.path.exists(path):
        return jsonify({"error": f"File not found at {path}"}), 404

    try:
        with open(path, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except json.JSONDecodeError as jde:
        return jsonify({"error": f"JSON decode error: {str(jde)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500