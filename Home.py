import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
selected2 = option_menu(None, ["Home", "DataVis", "Implementation"], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected2


