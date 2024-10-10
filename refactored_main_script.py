# Importing classes from file
from classes2 import WeatherDataFetcher, DataParser, UserInterface

# Main script
def main():
    while True:
        action = input("Actions:\n1. Get Weather Details\n2. Exit\nSelect Option(1 or 2): ")
        if action == "2":
            break
        elif action == "1":
            UserInterface()
        else:
            print("Invalid option. Please select '1' or '2'.")

if __name__ == "__main__":
    main()
