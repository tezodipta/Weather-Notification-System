# Weather Notification System

This Python script fetches weather data using the OpenWeather API and sends a notification to a Telegram user based on the weather conditions. It determines the weather type (cloudy, rainy, clear sky, etc.) for the next 12 hours and sends the appropriate message.

## Features
- Fetches weather data for a specific location using OpenWeather's OneCall API.
- Analyzes weather conditions using weather codes.
- Sends a Telegram message notifying the user about the weather.

---

## Prerequisites
Before running the script, ensure you have the following:
1. Python 3 installed on your system.
2. Required Python libraries:
   - `requests`

You can install the required library using pip:
```bash
pip install requests
```
An OpenWeather API key. Sign up at OpenWeather to obtain your API key.
A Telegram bot token and chat ID:
- Create a bot using the BotFather to get your bot token.
- Retrieve your chat ID by messaging your bot and checking the updates using Telegram's API.

## Code Overview

### Weather Conditions
The script categorizes weather based on OpenWeather's condition codes:

- Cloud: 801-804
- Atmosphere: 700-799
- Snow: 600-629
- Rain: 500-539
- Drizzle: 300-324
- Thunderstorm: 200-231
- Clear Sky: Code 800

### API Integration
- **Endpoint**: https://api.openweathermap.org/data/3.0/onecall
- **Parameters**:
  - `lat`: Latitude of the location.
  - `lon`: Longitude of the location.
  - `appid`: OpenWeather API key.
  - `exclude`: Specifies which data to exclude (current, minutely, daily).

### Telegram Message
- Sends a weather update using the Telegram Bot API.
- Example usage is provided to send a message to a specified chat ID.

## Configuration
Update the following variables in the script with your own details:
- `API_KEY`: Your OpenWeather API key.
- `chat_id`: Your Telegram chat ID.
- `bot_token`: Your Telegram bot token.
- `lat` and `lon`: Latitude and longitude of the desired location.

## How to Run
1. Clone or download the script.
2. Replace placeholder values with your API key, bot token, chat ID, and location details.
3. Run the script:
```bash
   python weather_notification.py
```

## Example Output
When the script runs successfully, it sends a message to your Telegram account with the weather update. Example response:
```json
{
  "ok": true,
  "result": {
    "message_id": 123,
    "chat": {
      "id": 1433257901,
      "type": "private"
    },
    "date": 1672531200,
    "text": "cloudy"
  }
}
```
## Notes
- Ensure the lat and lon values correspond to the location you want weather updates for.
- Keep your API key and bot token secure. Do not share them publicly.
- Replace the placeholders with actual values before running the script.



