from flask import Flask, send_from_directory, render_template
from resume.routes import resume_bp

app = Flask(__name__, template_folder="static/templates")

@app.route("/")
def home():
    return render_template("index.html")


app = Flask(__name__, static_folder="client/build", static_url_path="")
app.register_blueprint(resume_bp)

app = Flask(__name__)
app.register_blueprint(resume_bp)

