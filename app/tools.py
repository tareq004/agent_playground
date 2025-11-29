from loguru import logger

def get_weather(city: str):
    logger.info(f"Tool called: get_weather({city})")

    # Simulated weather (later you'll use real API)
    weather_data = {
        "Dhaka": "Sunny, 31°C",
        "Chittagong": "Cloudy, 28°C",
        "Sylhet": "Rainy, 25°C"
    }

    if city not in weather_data:
        return f"No data available for {city}"

    return weather_data[city]