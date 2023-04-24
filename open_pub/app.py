import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import image
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "open_pub")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "pub.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "cleaned_open_pub.csv")

st.title(" :beers: Open Pub Application :beers:")

st.header(":smile: Welcome to our Pub Finder Application :smile:")

# Displaying an image
img = image.imread(IMAGE_PATH)
st.image(img)

# Displaying our data set
df = pd.read_csv(DATA_PATH)
st.dataframe(df)

# Displaying Some Basic information

st.header("Some Basic Information about Dataset")
st.write(f"The dataset contains Total number of Pubs : **{len(df['name'].unique())}** ")
st.write(f"The dataset contains Total number of local authorities : **{len(df['local_authority'].unique())}** ")

# Statictic information
st.header("Some Basic Statistics about Dataset")
stats = df.describe().T
st.dataframe(stats)


