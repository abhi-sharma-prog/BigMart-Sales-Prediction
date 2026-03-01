import streamlit as st
import pandas as pd
import pickle
import joblib

st.title("🛒 BigMart Sales Prediction App")

st.write("Enter product details to predict sales")

pickle.dump(encoder, open("encoder.pkl", "wb"))

st.set_page_config(page_title="BigMart Sales Predictor", page_icon="🛒")
st.sidebar.header("About Project")
st.sidebar.write("Built by Abhishek Sharma")

# User Inputs
item_mrp = st.number_input("Item MRP", min_value=0.0)
outlet_size = st.selectbox("Outlet Size", ["Small", "Medium", "High"])
outlet_type = st.selectbox("Outlet Type", 
                           ["Grocery Store", "Supermarket Type1", 
                            "Supermarket Type2", "Supermarket Type3"])

# Create input dataframe
input_data = pd.DataFrame({
    "Item_MRP": [item_mrp],
    "Outlet_Size": [outlet_size],
    "Outlet_Type": [outlet_type]
})

if st.button("Predict Sales"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Sales: ₹ {prediction[0]:.2f}")