import streamlit as st
Name= st.text_input("Enter your Name: ")

Age = st.text_input("Enter your value of Age: ")

Sex= st.text_input("Enter your Sex: ")

# Weights in kg.
Weight = st.number_input("Enter your value of Weight: ",value=50)

# Height in meter square.
Height = st.number_input("Enter your value of Height: ",value=150)


# BMI is the Body Mass Index
BMI= float(Weight/(Height*Height))

if(BMI < 12):
    st.title('MalNutrition')
else:
    st.title('Not MalNutrition')