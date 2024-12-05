import streamlit as st
import utils as ut

ut.apply_base_style()

# st.set_page_config(page_title="Objectives", page_icon=":material/checklist:")

st.markdown("# Component Selection")
st.sidebar.header("")
st.write(
    """
Mocktail components:
- Container -> outsourced to Johan
    - QR code at the bottom
\n
- Liquid components
    - Coconut milk -> white tropical beaches
    - Pandan syrup -> exotic fragrance
\n
- Solid components (add textures and visual aspects)

    - Kaviar \n
        Pros:
        - Boosts the salty and Umami components
        - Luxurious

        Cons:
        - Expensive
        - Might not appeal to everyone

        -> Tapioca Balls with salty/Umami brown syrup -> perfect!

    - Diamonds \n
        Pros:
        - Luxurious

        Cons:
        - Expensive
        - Hard to digest

        -> Rock Sugar -> almost broke a tooth -> used to make the salty/Umami syrup
        -> Crushed ice -> just as sparkly and brings sensation -> perfect!

    - Fizzy powder \n
        Pros:
        - Sensation
        - Audible
        - Fun
        - Sour

        Cons:
        - None
    """
)

