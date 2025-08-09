import json
from flask import Blueprint, jsonify

resume_bp = Blueprint('resume', __name__, url_prefix='/api/resume')

@resume_bp.route('/meta', methods=['GET'])
def get_resume_meta():
    try:
        with open('resume_meta.json') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500