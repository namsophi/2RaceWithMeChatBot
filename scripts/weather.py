from pyowm.owm import OWM
from scripts.utils import text_to_speech
from geopy.geocoders import Nominatim
import datetime
import geocoder

# TODO: Fix api key exposure
owm = OWM('e9dd1343ae35d3b8db26656b78b75c45')
mgr = owm.weather_manager()
geolocator = Nominatim(user_agent="MyApp")


def get_current_weather(city):
    g = geolocator.geocode(city)
    one_call = mgr.one_call(lat=g.latitude, lon=g.longitude)
    weather_data = one_call.current
    response = _get_weather_statements(city, weather_data)
    cleaned_response = ' '.join(response)
    text_to_speech(cleaned_response)
    return cleaned_response


def _get_weather_statements(city, data):
    time = datetime.datetime.fromtimestamp(data.ref_time).date().strftime(
        'Today is %B %d of %Y')

    temperature = f"The current temperature here in {city} is " \
                  f"{data.temperature('celsius')['temp']}, and it feels like " \
                  f"{data.temperature('celsius')['feels_like']}"
    humidity = f"The humidity is {data.humidity} percent. " + \
               ("Not too humid today!" if data.humidity <= 50
                else "It's humid today!")
    rain = "It doesn't seem like it will rain today!" if data.rain == {} \
        else "There is a chance of rain today."
    overview = f"In general, today there will be {data.detailed_status}."
    return [time, temperature, humidity, rain, overview]
