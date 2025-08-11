from flask import Flask, render_template
from resume.routes import resume_bp

app = Flask(
    __name__,
    template_folder="/static/templates",       # assuming templates/ is in root
    static_folder="static",            # assuming static/ is in root
    static_url_path="/static"
)

app.register_blueprint(resume_bp)

@app.route("/")
def home():
    return render_template("index.html")