

# This is part of the refactored code, this section is used to define the class and functions.

class WeatherDataFetcher: 
    def __init__(self):
        self.city_weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
    
    def fetch_weather_data(self, requested_city):
        try:
            if requested_city in WeatherDataFetcher.city_weather_data.keys():
                return WeatherDataFetcher.city_weather_data.get(requested_city, {})
        except Exception as e:
            print(e)

    def display_weather(self, city):
        data = WeatherDataFetcher.fetch_weather_data(city, city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = DataParser.parse_weather_data(data, data)
            print(weather_report)

class DataParser:
    def parse_weather_data(self, data):
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

    def get_detailed_forecast(self, city):
        data = WeatherDataFetcher.fetch_weather_data(city, city)
        return DataParser.parse_weather_data(data, data)
        

class UserInterface:
    def __init__(self):
        option = input("Options:\n1. Get Detailed Weather Forecast\n2. Get Basic Weather Forecast\nSelect Option(1 or 2): ")
        if option == "1":
            city = input("Enter city to receive weather forecast: ")
            DataParser.get_detailed_forecast(city, city)
        elif option == "2":
            city = input("Enter city to receive weather forecast: ")
            WeatherDataFetcher.display_weather(city, city)
        else:
            print("Invalid option, please enter '1' or '2'.")
