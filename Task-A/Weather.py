# i used Streanlit to generate weather analysis project.
# reason for using Streanlit is that it is a powerful tool for data analysis and visualization.
# i used matplotlib for data visualization.
# i used requests for fetching data from API.
# i used datetime for handling date and time.

import streamlit as st
import requests
import matplotlib.pyplot as plt
import datetime
import os
from dotenv import load_dotenv
load_dotenv()


st.title("Welcome to Weather analysis")
st.markdown("## Here you can explore verious weather data plots for different cities around the world")

city_name = st.text_input("Enter city name : ", placeholder="Enter City Name")

# Method for return weather data from open weather api 
def weather_data():
    API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
    URL = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching data: {response.status_code}")
        return None

# When user Enter city name
if city_name:
    weather_data = weather_data()
    
    # When user enter valid city name
    if weather_data:
        forecast_list = weather_data["list"]
        dates = []
        temps = []
        minimum_temp = []
        maximum_temp = []
        feels_like = []
        humidity = []
        wind_speed = []

        # store weather data in lists
        for forecast in forecast_list:
            timestamp = forecast["dt"]
            date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M')
            temp = forecast["main"]["temp"]
            min_temp = forecast["main"]["temp_min"]
            max_temp = forecast["main"]["temp_max"]
            feels = forecast["main"]["feels_like"]
            hum = forecast["main"]["humidity"]
            wind = forecast["wind"]["speed"]

            dates.append(date)
            temps.append(temp)
            minimum_temp.append(min_temp)
            maximum_temp.append(max_temp)
            feels_like.append(feels)
            humidity.append(hum)
            wind_speed.append(wind)
            
        st.markdown("## Please select a category to visualize")
        st.write("for Ex : If you want to visualize temperature then select Temp")
        
        # Display 6 buttons in one line 
        column1, column2, column3, column4, column5, column6 = st.columns(6)
        with column1:
            show_temp = st.button("Temp")

        with column2:
            show_minimum_temp = st.button("Minimum Temp")
            
        with column3:
            show_maximum_temp = st.button("Maximum Temp")
            
        with column4:
            show_feels_like = st.button("Feels Like")

        with column5:
            show_humidity = st.button("Humidity")

        with column6:
            show_wind_speed = st.button("Wind Speed")
            
        # when Temp Button is clicked then display the Temprature graph
        if show_temp :
            st.subheader("Temperature Over Time")
            fig, ax = plt.subplots()
            ax.plot(dates, temps,linestyle='--',color='#36454F', marker='o',ms=7, markerfacecolor='green', markeredgecolor='red', label='Temperature')
            
            for i, txt in enumerate(temps):
                plt.annotate(txt, (dates[i], temps[i]), textcoords="offset points", xytext=(0,10), ha='center',rotation=90,fontsize=8)
                
            ax.set_xlabel("Date and Time")
            ax.set_ylabel("Temperature (°C)")
            ax.set_title(f"Temperature Forecast for {city_name}")
            plt.xticks(rotation=90)
            plt.grid()
            plt.legend()
            st.pyplot(fig)
            
        # when Minimum Temp Button is clicked then display the Minimum Temprature graph
        elif show_minimum_temp :
            st.subheader("Minimum Temperature Over Time")
            fig, ax = plt.subplots()
            ax.plot(dates, minimum_temp,linestyle='--',color='#36454F', marker='o',ms=7, markerfacecolor='lightgreen', markeredgecolor='red', label='Minimum Temperature')
            
            for i, txt in enumerate(minimum_temp):
                plt.annotate(txt, (dates[i], minimum_temp[i]), textcoords="offset points", xytext=(0,10), ha='center',rotation=90,fontsize=8)
                
            ax.set_xlabel("Date and Time")
            ax.set_ylabel("Minimum Temperature (°C)")
            ax.set_title(f"Temperature Forecast for {city_name}")
            plt.xticks(rotation=90)
            plt.grid()
            plt.legend()
            st.pyplot(fig)
            
        # when Maximum Temp Button is clicked then display the Maximum Temprature graph
        elif show_maximum_temp :
            st.subheader("Maximun Temperature Over Time")
            fig, ax = plt.subplots()
            ax.plot(dates, maximum_temp,linestyle='--',color='#36454F', marker='o',ms=7, markerfacecolor='red', markeredgecolor='lightgreen', label='Maximum Temperature')
            
            for i, txt in enumerate(maximum_temp):
                plt.annotate(txt, (dates[i], maximum_temp[i]), textcoords="offset points", xytext=(0,10), ha='center',rotation=90,fontsize=8)
                
            ax.set_xlabel("Date and Time")
            ax.set_ylabel("Maximum Temperature (°C)")
            ax.set_title(f"Temperature Forecast for {city_name}")
            plt.xticks(rotation=90)
            plt.grid()
            plt.legend()
            st.pyplot(fig)
            
        # when Feels Like Button is clicked then display the Feels Like graph
        elif show_feels_like :
            st.subheader("Feels Like Over Time")
            fig, ax = plt.subplots()
            ax.plot(dates, feels_like,linestyle='--',color='#36454F', marker='o',ms=7, markerfacecolor='yellow', markeredgecolor='red', label='Feels like')
            
            for i, txt in enumerate(feels_like):
                plt.annotate(txt, (dates[i], feels_like[i]), textcoords="offset points", xytext=(0,10), ha='center',rotation=90,fontsize=8)
                
            ax.set_xlabel("Date and Time")
            ax.set_ylabel("Feels Like")
            ax.set_title(f"Feels Like Forecast for {city_name}")
            plt.xticks(rotation=90)
            plt.grid()
            plt.legend()
            st.pyplot(fig)

        # when Humidity Button is clicked then display the Humidity graph
        elif show_humidity :
            st.subheader("Humidity Over Time")
            fig, ax = plt.subplots()
            ax.plot(dates, humidity,linestyle='--',color='#36454F', marker='o', markerfacecolor='lime', markeredgecolor='orange', label='Humidity')
            
            for i, txt in enumerate(humidity):
                plt.annotate(txt, (dates[i], humidity[i]), textcoords="offset points", xytext=(0,10), ha='center',rotation=90,fontsize=8)
            
            ax.set_xlabel("Date and Time")
            ax.set_ylabel("Humidity (%)")
            ax.set_title(f"Humidity Forecast for {city_name}")
            plt.xticks(rotation=90)
            plt.grid()
            plt.legend()
            st.pyplot(fig)
            
        # when Wind Speed Button is clicked then display the Wind Speed graph
        elif show_wind_speed :
            st.subheader("Humidity Over Time")
            fig, ax = plt.subplots()
            ax.plot(dates, wind_speed,linestyle='--',color='#36454F', marker='o', markerfacecolor='orange', markeredgecolor='lime', label='Wind Speed')
            
            for i, txt in enumerate(wind_speed):
                plt.annotate(txt, (dates[i], wind_speed[i]), textcoords="offset points", xytext=(0,10), ha='center',rotation=90,fontsize=8)
            
            ax.set_xlabel("Date and Time")
            ax.set_ylabel("Wind Speed")
            ax.set_title(f"Wund Speed Forecast for {city_name}")
            plt.xticks(rotation=90)
            plt.grid()
            plt.legend()
            st.pyplot(fig)

    # When user enter invalid city name
    else:
        st.warning("Please enter a valid city name.")