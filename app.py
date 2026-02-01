from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from caption import generate_caption

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists('uploads'):
    os.makedirs('uploads')

@app.route('/', methods=['GET', 'POST'])
def index():
    caption = ""
    image_url = ""
    if request.method == 'POST':
        if 'image' in request.files:
            file = request.files['image']
            if file.filename != "":
                path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
                file.save(path)
                caption = generate_caption(path)
                image_url = path
    return render_template('index.html', caption=caption, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
