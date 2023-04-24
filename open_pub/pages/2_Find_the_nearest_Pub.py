import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR)

DATA_PATH = os.path.join(dir_of_interest, "data", "cleaned_open_pub.csv")

# Loading our dataset
df = pd.read_csv(DATA_PATH)


st.title(" :beers: Open Pub Application :beers:")

st.header(" Find the nearest Pubs")

# Allow user to enter their latitude and longitude
lat = st.number_input("Enter your latitude:", value=51.95)
lon = st.number_input("Enter your longitude:", value=1.05)

# Define a function to calculate the Euclidean distance between two points
def euclidean_distance(lat1, lon1, lat2, lon2):
    return np.sqrt((lat1-lat2)**2 + (lon1-lon2)**2)

# Calculate the distance between the user's location and each pub in the dataset
df['distance'] = df.apply(lambda row: euclidean_distance(row['latitude'], row['longitude'], lat, lon), axis=1)

# Sort the dataset by distance and display the nearest 5 pubs
nearest_pubs = df.sort_values(by='distance').head(5)
st.write(f"Displaying the 5 nearest pubs to your location (lat: {lat}, lon: {lon}):")
st.dataframe(nearest_pubs)

# Create a map centered on the user's location
m = folium.Map(location=[lat, lon], zoom_start=13)

# Add a marker for the user's location
folium.Marker(location=[lat, lon], icon=folium.Icon(color='red'), popup='Your Location').add_to(m)

# Add markers for each of the nearest pubs
for index, row in nearest_pubs.iterrows():
    folium.Marker([row['latitude'], row['longitude']], popup=row['name']).add_to(m)

# Display the map
st.write("Map of the nearest pubs:")
folium_static(m)

