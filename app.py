from flask import Flask
from resume.routes import resume_bp  # make sure this import works

def create_app():
    app = Flask(__name__)
    app.register_blueprint(resume_bp)
    return app