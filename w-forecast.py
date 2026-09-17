import requests

print("===== Weather Application =====")

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=3"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        print("\nWeather Information:")
        print(response.text)
    else:
        print("Unable to get weather information.")

except requests.exceptions.RequestException as e:
    print("Error:", e)