import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
selected = option_menu(None, ["Home", "Learning", "Implementation"], 
    icons=['🏠', '🧑‍🏫', "👨‍🎨], 
    menu_icon="cast", default_index=0, orientation="horizontal")

selected


