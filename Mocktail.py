import streamlit as st
import utils as ut

ut.apply_base_style()

st.header("Sensolus Mocktail Challenge :material/local_bar: Team Fun")

# --- PAGE SETUP ---
project_objectives_page = st.Page(
    "views/01_Objectives.py",
    title="Objectives",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    "views/02_Product_Requirements.py",
    title="Product Requirements",
    icon=":material/checklist:",
)
project_3_page = st.Page(
    "views/03_Component_Selection.py",
    title="Component Selection",
    icon=":material/checklist:",
)
project_4_page = st.Page(
    "views/04_Sense-o-meter.py",
    title="Sense-o-meter",
    icon=":material/smart_toy:",
)
project_5_page = st.Page(
    "views/05_Component_Selection_pt2.py",
    title="Final",
    icon=":material/smart_toy:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
pg = st.navigation(pages=[project_objectives_page, project_2_page, project_3_page, project_4_page, project_5_page])

# --- SHARED ON ALL PAGES ---
st.logo("images/sensolus-logo.png")
# st.sidebar.markdown("Hallo mensen")

# --- RUN NAVIGATION ---
pg.run()
