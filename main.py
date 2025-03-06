import streamlit as st
import requests

st.title("Growth Mindset Challenge")
st.title("🕌 Namaz Timing App")
st.write("Get accurate prayer timings for your city.")

countries_cities = {
    "Pakistan": ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta"],
    "India": ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai"],
    "Saudi Arabia": ["Makkah", "Madinah", "Riyadh", "Jeddah", "Dammam"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "USA": ["New York", "Los Angeles", "Chicago", "Houston", "San Francisco"],
    "UK": ["London", "Manchester", "Birmingham", "Glasgow"],
    "Turkey": ["Istanbul", "Ankara", "Izmir", "Bursa"],
    "Malaysia": ["Kuala Lumpur", "Penang", "Johor Bahru"],
    "Bangladesh": ["Dhaka", "Chittagong", "Khulna"],
    "Indonesia": ["Jakarta", "Surabaya", "Bandung"],
    "Egypt": ["Cairo", "Alexandria", "Giza"],
    "Qatar": ["Doha", "Al Wakrah", "Al Khor"],
    "Canada": ["Toronto", "Vancouver", "Montreal", "Calgary"]
}


def prayer_time(city, country):
      url =  f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"
      response = requests.get(url)

      if response.status_code == 200:
          data = response.json()
          return data['data']['timings']
      else:
          return None

    
country = st.selectbox("Select your country:", list(countries_cities.keys()))
city = st.selectbox("Select your city:", countries_cities[country])


if st.button("Namaz Timing"):
      timings = prayer_time(city, country)
      if timings:
            st.success(f"Prayer Timings for {city}, {country}")
            prayer_timings_html = "<div style='padding: 20px; border-radius: 10px; border: 2px solid rgb(219, 52, 191); background-color: #f0f8ff;'>"
            prayer_timings_html += "<h4 style='color: rgb(219, 52, 191);'>All Prayer Timings</h4>"
            for prayer, time in timings.items():
               prayer_timings_html += f"<p style='color: rgb(119, 54, 59)><strong>{prayer}:</strong> {time}</p>"

      prayer_timings_html += "</div>"
      st.markdown(prayer_timings_html, unsafe_allow_html=True)
      
else:
        st.error("Failed to fetch prayer timings. Please check your city/country name.")

