import streamlit as st
import pandas as pd
import numpy as np
import pickle

model=pickle.load(open("LinearRegressionModel.pkl","rb"))
car=pd.read_csv("updated_car.csv")

st.title("Car Price Predictor")
st.markdown("---")
company=st.selectbox("Select the car company",options=sorted(car["company"].unique().tolist()),key=1)
y=[]
li=list(car["name"])
for i in li:
    if (i.split()[0] == company):
        y.append(i)
name=st.selectbox("Select the car model",options=y,key=2)
fuel_type=st.selectbox("Select the car company",options=sorted(car["fuel_type"].unique().tolist()),key=3)
Km_Driven=st.slider("Enter the total KM drive by the vehicle",min_value=car["kms_driven"].min(),
                    max_value=car["kms_driven"].max(),step=1,key=4)
year = st.slider("Select the manufacturing year", min_value=1999, max_value=2019, step=1,key=5)
button=st.button("Predict")
if button:
    result=model.predict(pd.DataFrame(columns=["name","company","year","kms_driven","fuel_type"],data=
                                      np.array([name,company,year,Km_Driven,fuel_type]).reshape(1,5)))
    if result < 0:
        st.header("No Price is Predicted Please contact to the customer Care")
    else:
        st.subheader("Predicted Price: ")
        st.subheader(np.round(result[0]))
