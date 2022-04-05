import streamlit as st
st.title('Decision Support System')
Name= st.text_input("Enter your Name: ")

Age = st.text_input("Enter your value of Age: ")

Sex= st.text_input("Enter your Sex: ")

# Weights in kg.
Weight = st.number_input("Enter your value of Weight: ",value=0)

# Height in meter square.
Height = st.number_input("Enter your value of Height: ",value=0)

# MUAC in Centi Meter
MUAC=st.number_input("Enter your value of Muac: ",value=0)


# BMI is the Body Mass Index
BMI= float(Weight/(Height*Height))

if(BMI < 12 or MUAC <12.5):
    st.header('MalNutrition')
else:
    st.header('Not MalNutrition')
