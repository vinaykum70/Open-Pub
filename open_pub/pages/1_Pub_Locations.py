import streamlit as st
import pandas as pd
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

st.header(" Find Pub Locations")

# Allow user to choose between searching by postal code or local authority
search_type = st.radio("Search by:", ('Postal Code', 'Local Authority'))

# Create a list of unique postal codes or local authorities to display in the dropdown menu
if search_type == 'Postal Code':
    search_list = sorted(df['postcode'].unique())
else:
    search_list = sorted(df['local_authority'].unique())

# Allow user to select a postal code or local authority from the dropdown menu
search_value = st.selectbox(f"Select a {search_type}:", search_list)

# Filter the dataset based on the selected postal code or local authority
if search_type == 'Postal Code':
    filtered_data = df[df['postcode'] == search_value]
else:
    filtered_data = df[df['local_authority'] == search_value]

# Display the filtered dataset
st.write(f"Displaying {len(filtered_data)} pubs in {search_value}:")
st.dataframe(filtered_data)


# Creating a map in centered on the chosen location
m = folium.Map(location=[filtered_data['latitude'].mean(), filtered_data['longitude'].mean()], zoom_start=13)

# Add markers for each pub in the filtered dataset
for index, row in filtered_data.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']], popup=row['name']).add_to(m)

# Displaying map
folium_static(m)





