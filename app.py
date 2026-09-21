#python -m venv env
#command .\env\Scripts\activate

# python -m pip install -r requirements.txt


import streamlit as st
import os 
from diet import bmi_calculator,bmr_calculator,tdee_calculator,calorie_target #here we import formula

# st.set_page_config(page_title="Health Assistant",page_icon="😊",layout="wide")

st.title("AI HEALTH ASSISTANT 😊")

st.write("Personal Health Assistance and Diet Recommendation Agent")
st.header("Health Information")

st.sidebar.header("🤷‍♂️Your Information")
##--------------------------------------------------------------------- for controls##

gender=st.sidebar.selectbox("Gender",['Male','Female'])
age=st.sidebar.number_input("Age",1,100)
weight=st.sidebar.number_input("Weight(kg)",1,120)
height=st.sidebar.number_input("Height(cm)",100,200)
activity=st.sidebar.selectbox("Activity",["Sedentary",
                                          "Lightly Active",
                                          "Moderately Active",
                                          "Very Active",
                                          "Extra Active"])
aim=st.sidebar.selectbox("AIM",["weight maintain","weight loss","weight gain"])

##----------------------------------------------------------------------------------------------###

bmi=bmi_calculator(weight,height)
bmr=bmr_calculator(gender,age,weight,height)                       #function call here
tdee=tdee_calculator(bmr,activity)
calorie=calorie_target(tdee,aim)

##----------------------------------------------------------------------------------------------------##

col1,col2,col3,col4=st.columns(4)
col1.metric("BMI",bmi)                               ##information show on interface by this all code
col2.metric("BMR",f"{bmr} Kcal")
col3.metric("TDEE",f"{tdee} Kcal")
col4.metric("Calorie Target",f"{calorie} Kcal")