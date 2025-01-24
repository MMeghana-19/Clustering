
import numpy as np
import pandas as pd
import streamlit as st
import pickle

#load all the instances tht are required
with open('model.pkl','rb') as file:
    model = pickle.load(file)
with open('scaler.pkl','rb') as file:
    scaler = pickle.load(file)
with open('pca.pkl','rb') as file:
    pca = pickle.load(file)


def prediction(input_data):
    scaled_data = ss.transform(input_data)
    pca_data = pca.transform(scaled_data)
    pred = model.predict(pca_data)[0]
    if pred ==0:
        return 'Developed'
    elif pred ==1:
        return ' Developing'
    else:
        return 'Under developed'

def main():
    st.title('HELP International Foundation')
    st.subheader('This application helps to classify the countrys need for funds on the basis of its socio-economic and health factors')
    child_mort = st.text_input('Enter child mortality rate')
    exports = st.text_input('Enter % of GDP spent on exports')
    health = st.text_input('Enter the % of GDP spent on health')
    imports = st.text_input('Enter % of of GDP spent on import')
    income = st.text_input('Enter country average income per person')
    inflation = st.text_input('Enter country inflation rate')
    life_expec = st.text_input('Enter country average life expectancy')
    total_fer = st.text_input('Enter country total fertility rate')
    gdpp = st.text_input('Enter country GDP per population rate')
    inp_list = [[child_mort,exports, health, imports, income, inflation, life_expec, total_fer, gdpp]]
    if st.button('Predict'):
        response = prediction(inp_list)
        st.success(response)

if __name__ == '__main__':
    main()
