import streamlit as st
import utils as ut

ut.apply_base_style()

# st.set_page_config(
#     page_title="Mocktail Challenge",
#     page_icon=":material/local_bar:",
# )
#st.sidebar.success("Select a page above.")


st.header("Sensolus Mocktail Challenge :material/local_bar: Team Fun 1")

# --- PAGE SETUP ---
project_objectives_page = st.Page(
    "views/01_Objectives.py",
    title="Objectives",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    "views/99_some_chart.py",
    title="Chart Example",
    icon=":material/smart_toy:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
pg = st.navigation(pages=[project_objectives_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
# pg = st.navigation(
#     {
#         "Info": [about_page],
#         "Projects": [project_1_page, project_2_page],
#     }
# )


# --- SHARED ON ALL PAGES ---
st.logo("images/sensolus-logo.png")
# st.sidebar.markdown("Hallo mensen")

# --- RUN NAVIGATION ---
pg.run()
