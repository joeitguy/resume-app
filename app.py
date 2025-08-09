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

@app.route('/view/badges')
def view_badges():
    return render_template('badges.html')

from flask import Flask, request, send_file, jsonify
import os

app = Flask(__name__)

# GET resume
@app.route('/resume', methods=['GET'])
def get_resume():
    return send_file('static/templates/resume.docx', mimetype='application/docx')

# GET cover letter (optional)
@app.route('/cover_letter', methods=['GET'])
def get_coverletter():
    return send_file('static/templates/coverletter.docx', mimetype='application/docx')

# GET Skills (optional)
@app.route('/skills', methods=['GET'])
def get_coverletter():
    return send_file('static/templates/skills.docx', mimetype='application/docx')


# PUT badge image
@app.route('/badges/<badge_id>/image', methods=['PUT'])
def upload_badge_image(badge_id):
    image = request.files['image']
    path = f'static/badges/{badge_id}.png'
    image.save(path)
    return jsonify({'status': 'uploaded', 'path': path})

# DELETE badge image
@app.route('/badges/<badge_id>/image', methods=['DELETE'])
def delete_badge_image(badge_id):
    path = f'static/badges/{badge_id}.png'
    if os.path.exists(path):
        os.remove(path)
        return jsonify({'status': 'deleted'})
    return jsonify({'error': 'Badge not found'}), 404

# GET all badge filenames
@app.route('/badges', methods=['GET'])
def list_badges():
    files = os.listdir('static/badges')
    return jsonify({'badges': files})

if __name__ == '__main__':
    app.run(debug=True)