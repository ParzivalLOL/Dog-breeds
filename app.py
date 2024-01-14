from flask import Flask, render_template, url_for, request
from ultralytics import YOLO
from PIL import Image
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    # If the user submits an empty form
    if file.filename == '':
        msg = 'No selected file'

    # Save the uploaded file to the upload folder

    # Process the image file (you can add your own image processing logic here)
    model = YOLO("C:/Users/shukl/OneDrive/Desktop/Programming/AI/dogAI/best.pt")
    file = request.files['file']
    image = Image.open(file)
    results = model(image)
    label = results[0].probs.top5
    breed = results[0].names[label[0]].title()
    if breed[0] == 'A' or 'E' or 'I' or 'O' or 'U':
        msg = "a " + breed
    else:
        msg = "a " + breed  
    
    return render_template('result.html', msg=msg)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
