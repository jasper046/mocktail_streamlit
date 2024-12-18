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

st.markdown("# Final  :material/forest:")
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
Pandan syrup replacement:
- Inspired by Coquito
- Replace pandan syrup with Coquito tea (fragrant)
""")
st.image("images/coquito.png", caption="Coquito")

st.write(
    """

\n
Umami syrup X-mas patch:
- Replace ginger/lemon with cherry/vanilla

\n
Fake caviar replacement:
- Replace with syrupy cherry
""")
st.image("images/xmas_syrup.png", caption="X-mas syrup production")

