from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)


util.load_data()
@app.route('/get_data')
def get_data():
    response = jsonify({
        'locations': util.get_data()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_estimated_price', methods=['POST'])
def predict_price():
    location = request.form['location']
    area = float(request.form['area'])
    rooms = float(request.form['rooms'])
    floor = float(request.form['floor'])
    rent = int(request.form['rent'])
    building_ownership = int(request.form['building_ownership'])
    construction_status = int(request.form['construction_status'])
    outdoor = int(request.form['outdoor'])
    heating = int(request.form['heating'])
    car = int(request.form['car'])


    response = jsonify({
        'estimated_price': util.get_estimated_price(location, area, rooms, floor, rent, building_ownership, construction_status, outdoor, heating, car)
    })

    return response


if __name__ == '__main__':
    app.run()
