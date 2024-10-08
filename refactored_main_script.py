# Importing classes from file
from refactored_weather_forecast_classes import CityWeatherData

# Main script
def main():
    weather = CityWeatherData()
    while True:
        option = input("Options:\n1. Get Weather Details\n2. Exit\nSelect Option(1 or 2): ")
        if option == "2":
            break
        elif option == "1":
            weather.parse_weather_data()
        else:
            print("Invalid option. Please select '1' or '2'.")

if __name__ == "__main__":
    main()