import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("house_price_model.pkl", "rb"))

st.title("House Price Prediction App")

# Get inputs for all 12 features
area = st.number_input("Area (sq ft)", min_value=0, max_value=10000, step=100)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, step=1)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=5, step=1)
stories = st.number_input("Stories", min_value=0, max_value=4, step=1)
mainroad = st.selectbox("Main Road Access", ["yes", "no"])
guestroom = st.selectbox("Guest Room", ["yes", "no"])
basement = st.selectbox("Basement", ["yes", "no"])
hotwaterheating = st.selectbox("Hot Water Heating", ["yes", "no"])
airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])
parking = st.number_input("Parking Spaces", min_value=0, max_value=5, step=1)
prefarea = st.selectbox("Preferred Area", ["yes", "no"])
furnishingstatus = st.selectbox("Furnishing Status", ["furnished", "semi-furnished", "unfurnished"])

# Convert categorical values to numerical
mainroad = 1 if mainroad == "yes" else 0
guestroom = 1 if guestroom == "yes" else 0
basement = 1 if basement == "yes" else 0
hotwaterheating = 1 if hotwaterheating == "yes" else 0
airconditioning = 1 if airconditioning == "yes" else 0
prefarea = 1 if prefarea == "yes" else 0
furnishing_map = {"furnished": 2, "semi-furnished": 1, "unfurnished": 0}
furnishingstatus = furnishing_map[furnishingstatus]

# Make prediction
if st.button("Predict Price"):
    features = np.array([[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, 
                          hotwaterheating, airconditioning, parking, prefarea, furnishingstatus]])
    price = model.predict(features)[0]
    st.success(f"Predicted House Price: ₹{round(price, 2)}")
