from flask import Flask, send_from_directory
from resume.routes import resume_bp

app = Flask(__name__, static_folder="client/build", static_url_path="")
app.register_blueprint(resume_bp)

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

app = Flask(__name__)
app.register_blueprint(resume_bp)

