
# This is my first attempt at the classes code, but kept getting same error over and over.

class WeatherDataFetcher: 
    def __init__(self):
        self.city_weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
    
    def fetch_weather_data(self, requested_city):
        try:
            if requested_city in self.city_weather_data.keys():
                return self.city_weather_data.get(requested_city, {})
        except Exception as e:
            print(e)

class DataParser:
    def parse_weather_data(self, requested_city):
        try:
            if requested_city in WeatherDataFetcher.city_weather_data.values():
                data = WeatherDataFetcher.fetch_weather_data(requested_city)
                city = data["city"]
                temperature = data["temperature"]
                condition = data["condition"]
                humidity = data["humidity"]
                print(f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%")
            else:
                raise ValueError
        except ValueError:
            print(f"Weather not found for {requested_city}.")

class UserInterface:
    def __init__(self):
        while True:
            action = input("Actions:\n1. Get Weather Details\n2. Exit\nSelect Option(1 or 2): ")
            if action == "2":
                break
            elif action == "1":
                city = input("Enter city to receive weather details: ")
                DataParser.parse_weather_data(city)
            else:
                print("Invalid option. Please select '1' or '2'.")
        




