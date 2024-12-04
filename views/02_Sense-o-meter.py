import streamlit as st
import utils as ut
import time
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd



def radar_chart(val):
    df = pd.DataFrame(dict(
    r=[1, 5, 2, 2, val],
    theta=['sweet','salty','sour',
           'bitter', 'umami']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    st.write(fig)

ut.apply_base_style()

# st.set_page_config(page_title="Plotting Demo", page_icon="📈")


st.markdown("# Sense-o-meter")
st.sidebar.header("Sense-o-meter")
st.write(
    """Tis model uses HI to optimize mocktail ingedients"""
)

status_text = st.sidebar.empty()


empty = st.empty()


# df = pd.DataFrame(dict(
#     r=np.array(r_base) * 2,
#     theta=['processing cost','mechanical properties','chemical stability',
#            'thermal stability', 'device integration']))

# fig = go.Figure()
# fig.add_trace(go.Scatterpolar(r=df['r'], theta=df['theta'], fill='toself', name='hoi'))
with empty.container():
    val = st.slider('Select value',0,10,1)
    radar_chart(val)

