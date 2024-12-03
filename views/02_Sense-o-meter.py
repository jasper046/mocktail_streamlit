import streamlit as st
import utils as ut
import time
import numpy as np
import plotly.express as px
import pandas as pd

ut.apply_base_style()

# st.set_page_config(page_title="Plotting Demo", page_icon="📈")


st.markdown("Sense-o-meter")
st.sidebar.header("Plotting Demo")
st.write(
    """With this model users can optimize mocktail ingedients to their liking using HI"""
)

status_text = st.sidebar.empty()

df = pd.DataFrame(dict(
    r=[1, 5, 2, 2, 3],
    theta=['processing cost','mechanical properties','chemical stability',
           'thermal stability', 'device integration']))
fig = px.line_polar(df, r='r', theta='theta', line_close=True)

chart = st.plotly_chart(fig)



# last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)
#
# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)
# progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
# st.button("Re-run")
