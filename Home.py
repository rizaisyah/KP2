import streamlit as st
from streamlit_option_menu import option_menu

selected = option_menu(
    None,
    ["Home", "Upload", "Tasks", "Settings"],
    icons=['house', 'cloud-upload', 'list-task', 'gear'],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

# Display the selected item
st.write(f"Selected: {selected}")


