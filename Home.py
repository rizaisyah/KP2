import streamlit as st
from streamlit_option_menu import option_menu
selected = option_menu(
  menu_title=None,  # required
  options=["Intro", "Learning", "Implementation"],  # required
  icons=["🏠", "🧑‍🏫", "👨‍🎨"],  # optional
  menu_icon="cast",  # optional
  default_index=0,  # optional
  orientation="horizontal",
        )
selected
