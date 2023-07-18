import streamlit as st

def main():
    st.title("My Streamlit App")

    # Menu options
    options = ["Home 🏠", "Upload 📤", "Tasks 📝", "Settings ⚙️"]

    # Display the selected item
    selected_option = st.empty()
    selected_option.write(f"Selected: {options[0]}")

    # CSS styling for the menu bar
    st.markdown("""
        <style>
            .menu-bar {
                display: flex;
                justify-content: center;
                background-color: #f0f0f0;
                padding: 10px;
                border-radius: 5px;
            }
            .menu-button {
                margin: 0 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Create a horizontal menu bar
    with st.container():
        col1, col2, col3, col4 = st.beta_columns(4)
        if col1.button("Home 🏠"):
            selected_option.write(f"Selected: {options[0]}")
        if col2.button("Upload 📤"):
            selected_option.write(f"Selected: {options[1]}")
        if col3.button("Tasks 📝"):
            selected_option.write(f"Selected: {options[2]}")
        if col4.button("Settings ⚙️"):
            selected_option.write(f"Selected: {options[3]}")

if __name__ == "__main__":
    main()
