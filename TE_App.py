import joblib
import seaborn as sns
import os
import streamlit as st

# EDA Pkgs
import pandas as pd
import numpy as np

# ML Pkgs


# Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# loading in the model to predict on the data
classifier = joblib.load('Thermal_Coefficent_Model.pkl')


def predict(C, Cr, Mn, Si, V, Mo, Temperature):
    N = classifier.predict([[float(C)/100, float(Cr)/100, float(Mn)/100, float(Si)/100,
                             float(V)/100, float(Mo)/100, float(Temperature)]])
    return N


def TE_Predictor_app():
    """ Data Processer and Visualizer  """
    html = """<img style="float: left; vertical-align:top" src="https://midhani-india.in/WordPress-content/uploads/2019/02/Midhani_Logo-with-tm.png">
    <img style="float: right; vertical-align:top" src="https://www.iitm.ac.in/themes/custom/iitm/assets/images/logo.png">
    <h1 style="text-align:center; font-size= 16px; margin-center">TC_Python</h1>
    prepared by Prof. G Phanikumar Group
     """
    st.markdown(html, unsafe_allow_html=True)
    st.title("Thermal Expanision Cofficent Predictor")
    st.subheader(
        "Predicts the Thermal Expanision Cofficent for given Composition")

    import joblib
    # loading in the model to predict on the data
    classifier = joblib.load('Thermal_Coefficent_Model.pkl')

    # defining the function which will make the prediction using
    # the data which the user inputs

    C = st.text_input("Carbon (C) (wt %) (0.02-0.05)")
    Cr = st.text_input("Chromium (Cr) (wt %)(4 -5.5)")
    Mn = st.text_input("Manganese (Mn) (wt %) (0.35-0.6)")
    Si = st.text_input("Silicon (Si) (wt %) (0.01-1)")
    V = st.text_input("Vanadium (V) (wt %) (0.33-1.22)")
    Mo = st.text_input("Molybdenum (Mo) (wt %) (0.5-2)")
    Temperature = st.text_input("Temperature (K) (623.15 - 873.15)")

    if st.button("Predict"):
        k = 0
        result = predict(C, Cr, Mn, Si, V, Mo, Temperature)
        st.success(
            'The Thermal Expanision Cofficent of the given Composition is {}'.format(result))


if __name__ == '__main__':
    TE_Predictor_app()
