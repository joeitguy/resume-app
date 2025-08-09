from flask import Flask, render_template, request, send_file, jsonify
import os

app = Flask(__name__)

# HTML routes
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

# File routes
@app.route('/resume', methods=['GET'])
def get_resume():
    return send_file('static/templates/resume.docx', mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')

@app.route('/cover_letter', methods=['GET'])
def get_coverletter():
    return send_file('static/templates/cover_letter.docx', mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')

@app.route('/skills', methods=['GET'])
def get_skills():
    return send_file('static/templates/skills.docx', mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')

# Badge image routes
@app.route('/badges/<badge_id>/image', methods=['PUT'])
def upload_badge_image(badge_id):
    image = request.files['image']
    path = f'static/badges/{badge_id}.png'
    image.save(path)
    return jsonify({'status': 'uploaded', 'path': path})

@app.route('/badges/<badge_id>/image', methods=['DELETE'])
def delete_badge_image(badge_id):
    path = f'static/badges/{badge_id}.png'
    if os.path.exists(path):
        os.remove(path)
        return jsonify({'status': 'deleted'})
    return jsonify({'error': 'Badge not found'}), 404

@app.route('/badges', methods=['GET'])
def list_badges():
    files = os.listdir('static/badges')
    return jsonify({'badges': files})

if __name__ == '__main__':
    app.run(debug=True)