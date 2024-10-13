

# This is part of the refactored code, this section is used to define the class and functions.

class WeatherDataFetcher: 
    def __init__(self):
        pass
           
    def fetch_weather_data(self, city):
    # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
    # Simulated data based on city
        weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
    }
        return weather_data.get(city, {})
   
class DataParser:
    def __init__(self): # Change this
        pass

    def display_detailed_weather(self, requested_city):
        data = WeatherDataFetcher.fetch_weather_data(requested_city, requested_city)
        if not data:
            print("Weather data not available")
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        print(f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%")

    def display_basic_weather(self, requested_city):
        data = WeatherDataFetcher.fetch_weather_data(requested_city, requested_city)
        if not data:
            print("Weather data not available")
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        return f"Weather in {city}: {temperature} degrees, {condition}."
        

class UserInterface:
    def __init__(self): # Change this
        pass

    def main(self):
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = DataParser.display_detailed_weather(city, city)
            else:
                forecast = DataParser.display_basic_weather(city, city)
                print(forecast)
