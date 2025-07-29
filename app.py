from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>Joe Bodden's Career Kit</h1>
    <ul>
        <li><a href="/static/_jbodden resume.docx">Resume</a></li>
        <li><a href="/static/_jbodden cover letter.docx">Cover Letter</a></li>
        <li><a href="/static/_jbodden Technical Skills Summary.docx">Skills Summary</a></li>
    </ul>
    """

