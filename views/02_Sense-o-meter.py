import streamlit as st
import utils as ut
import time
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd



def radar_chart(cm, um, ci):
    # df = pd.DataFrame(dict(
    # r=[1, 5, 2, 2, val],
    # theta=['sweet','salt','sour','bitter', 'umami']))
    # fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    # fig.update_traces(fill='toself')


    categories = ['sweet','salt','sour','bitter', 'umami']

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[80, cm, 30, ci, um],
        theta=categories,
        fill='toself',
        name='flavorprofile'))

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 100]
        )),
    font_size=16,
    legend_font_size=16,
    template = 'xgridoff',
    title = 'Flavor profile')

    st.write(fig)


ut.apply_base_style()

st.markdown("# Sense-o-meter")
st.sidebar.header('Ingredient Selector')
st.write(
    """Tis model uses HI to optimize mocktail ingedients \n \n"""
)


amount_coconutmilk = st.sidebar.slider('# Coconut Milk', min_value = 0, max_value = 100, value = 0)
amount_umamisyrup  = st.sidebar.slider('# Umami Syrup',  min_value = 0, max_value = 100, value = 0)
amount_crushedice  = st.sidebar.slider('# Crushed Ice',  min_value = 0, max_value = 100, value = 0)

Slider_Cursor = st.sidebar.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{
    background-color: rgb(84, 58, 194)} </style>''', unsafe_allow_html = True)

Slider_Number = st.sidebar.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div > div
                                { color: rgb(255, 255, 100); } </style>''', unsafe_allow_html = True)


radar_chart(amount_coconutmilk, amount_umamisyrup, amount_crushedice)

