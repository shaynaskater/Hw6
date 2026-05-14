# Using Streamlit, create a body mass index calculator app. It should take in height in feet or meters and weight in lbs or kilograms and return the associated body mass index.
# Return the python code in bmi.py and a gif screen capture of it running called bmi.gif.

# run streamlit
# streamlit run "/Users/shaynademick/Downloads/bmi.py"   

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
 
import streamlit as st

st.set_page_config(layout="wide")
st.markdown("# BMI calculator")
st.markdown("### Welcome to the BMI calculator! Please select your measurement system on the left before inputting your height and weight.")

data_type = st.sidebar.radio("Data type", ["Metric", "Customary/Imperial"])

if data_type == "Metric":
    numbera = st.number_input("Input height in meters", value=None, placeholder="Type a number...")
    if numbera is not None:
        st.write(f"Your height is {numbera:.2f} meters")

    numberb = st.number_input("Input weight in kilograms", value=None, placeholder="Type a number...")
    if numberb is not None:
        st.write(f"Your weight is {numberb:.2f} kilograms")

    if numbera and numberb:
        bmi = numberb / (numbera ** 2)
        st.write(f"Your BMI is {bmi:.2f}")

else:
    col1, col2 = st.columns(2)
    with col1:
        feet = st.number_input("Height (feet)", value=None, placeholder="Feet...", min_value=0)
    with col2:
        inches = st.number_input("Height (inches)", value=None, placeholder="Inches...", min_value=0, max_value=11)

    total_inches = (feet or 0) * 12 + (inches or 0)
    if feet is not None:
        st.write(f"Your height is {int(feet or 0)} ft {int(inches or 0)} in")

    numberb = st.number_input("Input weight in lbs", value=None, placeholder="Type a number...")
    if numberb is not None:
        st.write(f"Your weight is {numberb:.2f} lbs")

    if feet is not None and numberb and total_inches > 0:
        bmi = (numberb / (total_inches ** 2)) * 703
        st.write(f"Your BMI is {bmi:.2f}")

st.write("### BMI Categories ###")
st.write("- Underweight: BMI less than 18.5")
st.write("- Normal weight: BMI between 18.5 and 24.9")
st.write("- Overweight: BMI between 25 and 29.9")
st.write("- Obesity: BMI 30 or greater")
# bmi categories from https://www.youtube.com/watch?v=Z4uhilpTe9k