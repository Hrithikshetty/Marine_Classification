from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin

import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'




model = load_model('C:\\Users\\aloky\\OneDrive\\Desktop\\Marine_Classification\\Models\\Classification\\marine_model.h5')

class_names = ['Bangus', 'Big Head Carp', 'Black Spotted Barb', 'Catfish', 'Climbing Perch', 'Fourfinger Threadfin', 'Fresherwater Eel', 'Glass Perchlet', 'Goby', 
               'Gold Fish', 'Gourami', 'Grass Crap', 'Green Spotted Puffer', 'Indian Carp', 'Indo Pacific Tarpon', 'Jaguar Fish', 'Janitor Fish', 'Knifefish',
               'Long Snouted Pipefish', 'Mosquito Fish', 'Mudfish', 'Mullet', 'Pangasius', 'Perch', 'Scat Fish', 'Silver Barb', 'Silver Carp', 'Silver Perch', 
               'Snakehead', 'Tenpounder', 'Tilapia']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'OPTIONS'])  
@cross_origin()

def predict():
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'CORS preflight request successful'})
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response

    file = request.files['file'] 
    if not file:
        print("not found")
        return jsonify({'error': 'No file found in the request'}), 400

    file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    opencv_image = cv2.resize(opencv_image, (224, 224))
    opencv_image = preprocess_input(opencv_image) 
    opencv_image = np.expand_dims(opencv_image, axis=0)

    y_pred = model.predict(opencv_image)
    result = class_names[np.argmax(y_pred)]

    # Return both the predicted class name and the image file
    
    # response.headers.add('Access-Control-Allow-Origin', '*') 
    response = jsonify({"message": result})
    # print(response) # Allow all origins
    # response="hello"
    # response = jsonify({'prediction': prediction})
    return response
    # print(response)


if __name__ == '__main__':
    app.run(debug=True, port=50603)
