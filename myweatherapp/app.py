from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


# Home API
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Weather API is running",
        "usage": "/weather?city=London"
    })


# Weather API
@app.route('/weather', methods=['GET'])
def get_weather():

    # Get city from URL
    city = request.args.get('city')

    # Check whether city was provided
    if not city:
        return jsonify({
            "error": "Please provide a city name"
        }), 400

    # Open-Meteo Geocoding API
    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

    geocoding_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    try:
        # Call external Geocoding API
        geo_response = requests.get(
            geocoding_url,
            params=geocoding_params
        )

        geo_data = geo_response.json()

        # Check whether city was found
        if "results" not in geo_data:
            return jsonify({
                "error": "City not found"
            }), 404

        # Get latitude and longitude
        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        city_name = location["name"]
        country = location.get("country", "")

        # Open-Meteo Weather API
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
        }

        # Call external Weather API
        weather_response = requests.get(
            weather_url,
            params=weather_params
        )

        weather_data = weather_response.json()

        # Get current weather
        current_weather = weather_data["current"]

        # Return our own JSON response
        return jsonify({
            "city": city_name,
            "country": country,
            "latitude": latitude,
            "longitude": longitude,
            "temperature": current_weather["temperature_2m"],
            "humidity": current_weather["relative_humidity_2m"],
            "wind_speed": current_weather["wind_speed_10m"],
            "temperature_unit": weather_data["current_units"]["temperature_2m"],
            "wind_speed_unit": weather_data["current_units"]["wind_speed_10m"]
        })

    except requests.exceptions.RequestException as e:

        return jsonify({
            "error": "Unable to connect to weather service",
            "details": str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True)