import os
import json
from flask import Blueprint, jsonify

resume_bp = Blueprint('resume', __name__, url_prefix='/api/resume')

@resume_bp.route('/meta', methods=['GET'])
def get_resume_meta():
    # Construct absolute path to /api/resume_meta.json
    path = os.path.join(os.path.dirname(__file__), '..', 'resume_meta.json')
    path = os.path.abspath(path)

    try:
        with open(path) as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
