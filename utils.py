import streamlit as st

def apply_base_style():
    st.markdown("""
    <style>
    .stApp {
        font-family: Lato, sans-serif
        color: white;
        background-color: #171d3a;
    }
    body {
        color: white;
    }
    h1 {
        color: white;
        font-size: 40px;
    }
    h2 {
        color: white;
        font-size: 30px;
    }
    p {
        color: white;
        font-size: 20px;
    }
    div {
        color: white;
        font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

