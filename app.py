import pandas as pd
import streamlit as st
import plotly.express as px

# Load custom CSS and JavaScript
def load_custom_css(file_path):
    with open(file_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def load_custom_js(file_path):
    with open(file_path) as f:
        st.markdown(f'<script>{f.read()}</script>', unsafe_allow_html=True)

load_custom_css("assets/style.css")
load_custom_js("assets/script.js")

# Load the preprocessed dataset
data_path = 'data/covid.csv'
data = pd.read_csv(data_path)

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Create a list of unique countries
countries = data['Country'].unique()

# Streamlit app layout
st.title("COVID-19 Data Visualization Dashboard")
st.sidebar.title("Settings")

# Sidebar - Country selection
selected_country = st.sidebar.selectbox("Select a Country", countries)

# Filter data for the selected country
country_data = data[data['Country'] == selected_country]

# Plot the data
fig = px.line(country_data, x='Date', y='Daily New Cases per Million',
              title=f'Daily New Confirmed Cases of COVID-19 per Million People in {selected_country}',
              labels={'Date': 'Date', 'Daily New Cases per Million': 'Daily New Cases per Million'})

# Display the plot
st.plotly_chart(fig)

# Display the raw data
if st.checkbox("Show raw data"):
    st.write(country_data)