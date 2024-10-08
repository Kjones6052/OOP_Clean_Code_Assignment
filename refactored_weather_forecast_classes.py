
# This is part of the refactored code, this section is used to define the class and functions.

# Create a class to hold City Weather Data
class CityWeatherData:
    def __init__(self):
        self.city_weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }

    def fetch_weather_data(self, city):
        # Print statement to inform process initialized
        print(f"Fetching weather data for {city}")
        # Fetch the weather data
        return self.city_weather_data.get(city, {})

    def parse_weather_data(self):
        requested_city = input("Enter city to receive weather details: ")
        # Parse weather dict for individual weather details:
        try:
            if requested_city in self.city_weather_data.values():
                data = self.fetch_weather_data(requested_city)
                city = data["city"]
                temperature = data["temperature"]
                condition = data["condition"]
                humidity = data["humidity"]
                # Use print statement to deliver the weather details:
                print(f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%")
            else:
                raise ValueError
        except ValueError:
            print(f"Weather not found for {requested_city}.")



