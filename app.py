from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/view/resume')
def view_resume():
    return render_template('resume.html')

@app.route('/view/cover-letter')
def view_cover_letter():
    return render_template('cover_letter.html')

@app.route('/view/skills')
def view_skills():
    return render_template('skills.html')

@app.route('/view/design_page')
def view_design_page():
    return render_template('design_page.html')

@app.route('/view/static/badges')
def view_badges():
    return render_template('badges.html')