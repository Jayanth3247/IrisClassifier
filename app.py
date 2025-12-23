import streamlit as st
import joblib

model = joblib.load('knnmodel.joblib')

st.title('Iris Classification Project')
st.text('This is a project developed by Jayanth')

sl = st.number_input("Enter the sepal length: ")
sw = st.number_input("Enter the sepal width: ")
pl = st.number_input("Enter the petal length: ")
pw = st.number_input("Enter the petal width: ")

if st.button('Predict Flower'):
    prediction = model.predict([[sl,sw,pl,pw]])
    if prediction==0:
        st.write('Flower 1')
    elif prediction==1:
        st.write('Flower 2')
    else:
        st.write('Flower 3')