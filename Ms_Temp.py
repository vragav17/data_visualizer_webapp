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
import seaborn as sns



def MsT_app():
    """ Data Processer and Visualizer  """
    html = """<img style="float: left; vertical-align:top" src="https://midhani-india.in/WordPress-content/uploads/2019/02/Midhani_Logo-with-tm.png">
    <img style="float: right; vertical-align:top" src="https://www.iitm.ac.in/themes/custom/iitm/assets/images/logo.png">
    <h1 style="text-align:center; font-size= 16px; margin-center">TC_Python</h1>
    prepared by Prof. G Phanikumar Group
     """
    st.markdown(html, unsafe_allow_html = True)
    st.title("Martensite Start Temperature Predictor")
    st.subheader("Predicts the Ms Temperature for given Composition")

    import pickle
    # loading in the model to predict on the data
    pickle_in = open('classifier.pkl', 'rb')
    classifier = pickle.load(pickle_in)

    # defining the function which will make the prediction using
    # the data which the user inputs
    def prediction(C, Mn, Si,Cr, Ni, Mo, V, Co, W):

        prediction = classifier.predict(
            [[C, Mn, Si,Cr, Ni, Mo, V, Co, W, 0,0, 0,0,0,0]])
        print(prediction)
        return prediction

    C = st.text_input("Carbon (C) (wt %) (0.0-2.25)")
    Mn = st.text_input("Manganese (Mn) (wt %)(0.0-10.24)")
    Si = st.text_input("Silicon (Si) (wt %) (0.0-3.8)")
    Cr  = st.text_input("Chromium (Cr) (wt %) (0.0-17.98)")
    Ni = st.text_input("Nickel (Ni) (wt %) (0.0-31.54)")
    Mo = st.text_input("Molybdenum (Mo) (wt %) (0.0-8.0)")
    V = st.text_input("Vanadium (V) (wt %) (0.0-4.55)")
    Co = st.text_input("Cobalt (Co) (wt %) (0.0-16.08)")
    W = st.text_input("Tungsten (W) (wt %) (0.0-18.59)")


    if st.button("Predict"):
        k = 0
        result = prediction(C, Mn, Si,Cr, Ni, Mo, V, Co, W)
        st.success('The Ms Temperature of the given alloy is {}'.format(result))
if __name__ == '__main__':
    MsT_app()
