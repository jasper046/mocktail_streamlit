import streamlit as st
import utils as ut

ut.apply_base_style()

st.markdown("# Product Requirements :material/checklist:")
st.sidebar.header("")
st.write(
    """
Product Requirements:
1) Qualify as a mocktail:
- Beef Rendang (Beef stew)  --> does not qualify, dropped
- Chicken Satay (Chicken skewers)  --> does not qualify, dropped
- Steamed pandang cake  --> does not qualify, dropped
- Non-alcholic beverage --> qualifies, but needs to be developed

2) Sensolus -> Sensational mocktail:
It has to appeal to the senses
- Taste: Sweet, Sour. Salty, Bitter, Umami
- Look: Shape, Colors, Presentation
- Feel: Texture, Viscosity
- Smell: Different Aroma's
- Hear: Audible component

3) Fun
- Enjoying the process:
    - Rewarding to put your best effort and take the assignment at hand seriously: e.g. a Mocktail challenge
- Reaping the benefits and sharing with your colleagues:
    - Luxurious life on white sandy beaches on Exotic Islands
- If 2) is implemented correctly, it should be fun to drink

    """
)

