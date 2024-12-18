import streamlit as st
import utils as ut

ut.apply_base_style()

st.markdown("""
    <style>
    .stApp {
        background-image: "images/xmas_background.jpeg";
        background-color: #bb0a26;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("# Final")
st.sidebar.header("")
st.write(
    """
Add X-mas spirit patches:
- Limit colors to red and white
- Add typical X-mas flavour profile

\n
Fizzy powder replacement:
- Replace with powder sugar

\n
Pandan syrup:
- Inspired by Coquito
""")
st.image("images/coquito.png", caption="Coquito")

st.write(
    """
-> Replace pandan syrup with Coquito tea:
- Similar

\n
Umami syrup:
- Replace ginger/lemon with cherry/vanilla

\n
Fake caviar:
- Replace with syrupy cherry
""")
st.image("images/xmas_syrup.png", caption="X-mas syrup production")

