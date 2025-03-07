import streamlit as st
import google.generativeai as genai
import pandas as pd
from config import API_KEY

# Configure Gemini API
genai.configure(api_key=API_KEY)

def get_pollution_data():
    """Fetches industries and other causes of air pollution using Gemini API."""
    prompt = "List major industries and other causes of air pollution in a structured format. Include industry types and specific pollutants they emit."
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    
    # Parse response into structured data (assuming CSV-like output)
    data = []
    for line in response.text.split("\n"):
        columns = line.split(",")
        if len(columns) == 3:  # Expecting 3 columns (Industry, Cause, Pollutants)
            data.append(columns)
    
    return pd.DataFrame(data, columns=["Industry", "Cause", "Pollutants"])

# Streamlit UI
st.title("Air Pollution Sources")
st.write("This table presents industries and other causes of air pollution.")

data = get_pollution_data()
st.dataframe(data)
