import os
import json
from flask import Blueprint, jsonify

resume_bp = Blueprint("resume", __name__, url_prefix="/api/resume")

@resume_bp.route("/meta", methods=["GET"])
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
    
@resume_bp.route("/health", methods=["GET"])
def health_check():
    print("[DEBUG] /health route hit")
    return jsonify({"status": "ok"}), 200

from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder="client/build")

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(app.static_folder, path)

from flask import send_from_directory

@app.route("/static/<path:filename>")
def serve_resume(filename):
    return send_from_directory("static", filename)

