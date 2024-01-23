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
    path_to_best_pt = "best.pt"
    try:
        mod = YOLO(path_to_best_pt)
    except Exception as e:
        return (f"Error initializing YOLO model: {e}")
    # Add additional logging or handle the exception appropriately

    file = request.files['file']
    image = Image.open(file)
    results = mod.predict(image)
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
