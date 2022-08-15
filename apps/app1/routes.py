from flask import Blueprint, request
from scripts.greeting import certain_greeting, uncertain_greeting
from scripts.weather import get_current_weather
from scripts.location import get_location_data
from scripts.distance import get_distance_affirmation
app1 = Blueprint('app1', __name__)


@app1.route("/greeting")
def greeting():
    certainty = request.args["certainty"]
    name = request.args["name"]
    if certainty == "certain":
        response = certain_greeting(name)
        return response
    else:
        response = uncertain_greeting(name)
        return response


@app1.route('/weather')
def weather():
    weather_location = request.args["location"]
    response = get_current_weather(weather_location)
    return response


@app1.route('/location')
def location():
    city = request.args["city"]
    country = request.args["country"]
    response = get_location_data(city, country)
    return response


@app1.route('/distance')
def distance():
    travelled = request.args["travelled"]
    response = get_distance_affirmation(travelled)
    return response

