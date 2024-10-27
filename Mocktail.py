import streamlit as st

# with open( "static/style.css" ) as css:
#     st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.set_page_config(
    page_title="Mocktail Challenge",
    page_icon=":material/local_bar:",
)
st.sidebar.success("Select a page above.")

st.write("# Sensolus Mocktail Challenge :material/local_bar:")

st.subheader("Team Fun 1")

st.markdown("Bladibladibla", unsafe_allow_html = True)


