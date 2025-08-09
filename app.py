from flask import Flask
from resume.routes import resume_bp

app = Flask(__name__)
app.register_blueprint(resume_bp)

