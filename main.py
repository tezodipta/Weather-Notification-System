import requests

Cloud = range(801,805)
Atmosphere = range(700,800)
Snow = range(600,630)
Rain = range(500,540)
Drizzle = range (300,325)
Thunderstorm = range(200,232)


# open weather info
endpoint = "https://api.openweathermap.org/data/3.0/onecall"
API_KEY = "Your api key"

parameter = {
    "lat":123,      #your latitude
    "lon":123,      #your longitude
    "appid":API_KEY,
    "exclude": "current,minutely,daily"

}

# fetching api
response = requests.get(url=endpoint,params=parameter)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

# will_rain = False


for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) in Cloud:
        result = "cloudly"
    elif int(condition_code) in Atmosphere:
        result = "mist,dust,smoke"
    elif int(condition_code) in Snow:
        result = "Rain or snow"
    elif int(condition_code) in Rain:
        result = "Rainy"
    elif int(condition_code) in Drizzle:
        result = "Drizzle"
    elif int(condition_code) in Thunderstorm:
        result = "Thinderstrom"
    elif int(condition_code) == 800:
        result = "clear sky"
    
def send_message(chat_id, text, bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    response = requests.post(url, data=payload)
    return response.json()


# Example usage
chat_id = ''  # Replace with the actual chat ID
bot_token = ''  # Replace with your bot's token
message = result
response = send_message(chat_id, message, bot_token)
print(response)
    