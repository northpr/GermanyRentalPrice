from flask import Flask, request, jsonify
import util
app = Flask(__name__)


@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'heattype': util.get_heattype_names(),
        'roomcon': util.get_roomcon_names(),
        'flattype': util.get_flattype_names(),
        'locations': util.get_location_names()
            })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response



@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    livingSpace = float(request.form['livingSpace']) # total living space
    noRooms = float(request.form['noRooms']) # Number of rooms
    additionCost = float(request.form['additionCost']) #electrical, etc

    heating_type = request.form['heating_type'] # heater type
    condition = request.form['condition']
    typeOfFlat = request.form['typeOfFlat']
    regio2 = request.form['regio2']

    response = jsonify({
        'estimated_price': util.get_estimated_price(livingSpace,noRooms,additionCost,heating_type,condition,typeOfFlat,regio2)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Germany Rental Price Prediction")
    util.load_saved_artifacts()
    app.run()