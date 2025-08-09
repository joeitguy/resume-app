from flask import Blueprint, jsonify

resume_bp = Blueprint('resume', __name__, url_prefix='/api/resume')

@resume_bp.route('/meta', methods=['GET'])
def get_meta():
    return jsonify({
        "name": "Joseph W.P. Bodden Jr.",
        "title": "Integration & Data Engineer",
        "location": "San Diego, CA",
        "email": "joeitguy@gmail.com",
        "phone": "(858) 225-0733",
        "linkedin": "https://linkedin.com/in/joeitguy"
    })