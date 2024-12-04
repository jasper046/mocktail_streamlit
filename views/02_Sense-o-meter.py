import streamlit as st
import utils as ut
import time
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

categories =          ['sweet','salt',  'sour','bitter', 'umami', 'fragrant', 'refreshing']
profile_umamisyrup  = [90,       40,    70,      15,        60,     23,         3]
profile_coconutmilk = [40,       15,    2,       20,        8,      60,         28]
profile_crushedice  = [0,        0,     0,       0,         0,      0,          100]
profile_pandansyrup = [100,      0,     13,      0,         12,     200,        0]



def radar_chart(us, cm, ps, ci):

    profile = np.array((us * np.array(profile_umamisyrup)) + (cm * np.array(profile_coconutmilk)) + (ps * np.array(profile_pandansyrup)) + (ci * np.array(profile_crushedice))) * 5 / (200 + us + cm + ps + ci)


    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=profile,
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

amount_umamisyrup   = st.sidebar.slider('# Umami Syrup',  min_value = 0, max_value = 100, value = 0)
amount_coconutmilk  = st.sidebar.slider('# Coconut Milk', min_value = 0, max_value = 100, value = 0)
amount_pandansyrup  = st.sidebar.slider('# Pandan Syrup',  min_value = 0, max_value = 100, value = 0)
amount_crushedice   = st.sidebar.slider('# Crushed Ice',  min_value = 0, max_value = 100, value = 0)

# Slider_Cursor = st.sidebar.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{
#     background-color: rgb(84, 58, 194)} </style>''', unsafe_allow_html = True)
#
# Slider_Number = st.sidebar.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div > div
#                                 { color: rgb(255, 255, 100); } </style>''', unsafe_allow_html = True)


radar_chart(amount_umamisyrup, amount_coconutmilk, amount_pandansyrup, amount_crushedice)

