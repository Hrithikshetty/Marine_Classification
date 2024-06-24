from flask import Flask, render_template, request
from flask_cors import CORS
from Classification import classify
from alternateRoutes import alternateRoutes

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html', message = None)

@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    if request.method == 'POST':
        file = request.files['file'] 
        if file:
            response = classify(file)
            return response 
        else :
            return "No file Selected!!!"
    return render_template('predict.html', message = None)

@app.route('/alternateRoute', methods = ['POST','GET'])
def alternateRoute():
    if request.method == 'POST':
        user_location = request.form['location']
        user_fish_species = request.form['fish_species']
        nearest_places, map_path = alternateRoutes(user_location, user_fish_species)
        if nearest_places == "Invalid Fish Request" or nearest_places == "Invalid Location":
            return render_template('alternateRoute.html', message="Invalid Location or Fish Details!!!")
        return render_template('alternateRoute.html', location=user_location, fish_species=user_fish_species, nearest_places=nearest_places, map_path=map_path)
    return render_template('alternateRoute.html', message=None) 

if __name__ == '__main__':
    app.run(debug=True)
