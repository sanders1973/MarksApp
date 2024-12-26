import streamlit as st

import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        return temperature
    else:
        st.error("Error: Could not retrieve weather data.")
        return None

def main():
    st.title("Current Temperature Checker")

    api_key = st.text_input("Enter your OpenWeatherMap API Key:", type="password")
    location = st.text_input("Enter your location (e.g., city name):")

    if st.button("Get Temperature"):
        if api_key and location:
            temperature = get_weather(api_key, location)
            if temperature is not None:
                st.success(f"The current temperature in {location} is {temperature}°C.")
        else:
            st.error("Please enter both API key and location.")

if __name__ == "__main__":
    main()
