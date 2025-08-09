from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

# 📁 Paths
DOCS_DIR = os.path.abspath("docs")  # Adjust if needed
TEMPLATES_DIR = os.path.abspath("templates")

# 🧾 Static File Endpoints
@app.route("/resume")
def serve_resume():
    return send_from_directory(DOCS_DIR, "_jbodden resume.docx")

@app.route("/cover_letter")
def serve_cover_letter():
    return send_from_directory(DOCS_DIR, "_jbodden cover letter.docx")

@app.route("/skills_summary")
def serve_skills():
    return send_from_directory(DOCS_DIR, "_jbodden Technical Skills Summary.docx")

# 🖼️ HTML Views
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/view/resume")
def view_resume():
    return render_template("resume.html")

@app.route("/view/cover_letter")
def view_cover_letter():
    return render_template("cover_letter.html")

@app.route("/view/skills")
def view_skills():
    return render_template("skills.html")

@app.route("/view/badges")
def view_badges():
    return render_template("badges.html")

@app.route("/view/design")
def view_design():
    return render_template("design_page.html")

# 🩺 Health Check
@app.route("/ping")
def ping():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)