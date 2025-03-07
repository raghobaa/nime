import streamlit as st
import google.generativeai as genai
import pandas as pd
from config import API_KEY

# Configure Gemini API
genai.configure(api_key=API_KEY)

def get_pollution_data():
    """Fetches industries and other causes of air pollution using Gemini 1.5 API."""
    prompt = (
        "Provide a structured table of major industries and other sources of air pollution. "
        "Include industry type, specific causes, and pollutants emitted. Format as CSV-like output: "
        "'Industry, Cause, Pollutants'."
    )
    
    model = genai.GenerativeModel("gemini-1.5-pro")  # Use Gemini 1.5
    response = model.generate_content(prompt)
    
    # Ensure the response contains valid text
    if not response.text:
        return pd.DataFrame(columns=["Industry", "Cause", "Pollutants"])
    
    # Parse response into structured data
    data = []
    for line in response.text.strip().split("\n"):
        columns = line.split(",")
        if len(columns) == 3:  # Expecting 3 columns (Industry, Cause, Pollutants)
            data.append([col.strip() for col in columns])
    
    return pd.DataFrame(data, columns=["Industry", "Cause", "Pollutants"])

# Streamlit UI
st.title("Air Pollution Sources")
st.write("This table presents industries and other causes of air pollution.")

data = get_pollution_data()
st.dataframe(data)
