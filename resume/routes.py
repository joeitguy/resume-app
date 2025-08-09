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
    
    import os
from flask import jsonify

@app.route('/api/resume/meta')
def resume_meta():
    path = os.path.join(os.path.dirname(__file__), 'resume_meta.json')
    try:
        with open(path) as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})
