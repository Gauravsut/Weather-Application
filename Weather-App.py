import requests

def get_weather_data():
    url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"  # Replace with the actual API URL
    
   
    response = requests.get(url)
    data = response.json()
    
    return data["list"]

def get_weather_by_date(weather_data, date):
    for item in weather_data:
        if item["dt_txt"].startswith(date):
            return item["main"]["temp"]
    return None

def get_wind_speed_by_date(weather_data, date):
    for item in weather_data:
        if item["dt_txt"].startswith(date):
            return item["wind"]["speed"]
    return None

def get_pressure_by_date(weather_data, date):
    for item in weather_data:
        if item["dt_txt"].startswith(date):
            return item["main"]["pressure"]
    return None

def main():
    weather_data = get_weather_data()
    
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            date = input("Enter the date (YYYY-MM-DD): ")
            temp = get_weather_by_date(weather_data, date)
            if temp is not None:
                print(f"Temperature on {date}: {temp} K")
            else:
                print("Data not found for the given date.")
        
        elif choice == 2:
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed_by_date(weather_data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Data not found for the given date.")
        
        elif choice == 3:
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure_by_date(weather_data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not found for the given date.")
        
        elif choice == 0:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
