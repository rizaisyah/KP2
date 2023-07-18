import streamlit as st

def main():
    st.title("My Streamlit App")

    # Menu options
    options = ["Home 🏠", "Upload 📤", "Tasks 📝", "Settings ⚙️"]

    # Display the selected item
    selected_option = st.empty()
    selected_option.write(f"Selected: {options[0]}")

    # Create a horizontal menu bar
    menu_col1, menu_col2, menu_col3, menu_col4 = st.beta_columns(4)

    if menu_col1.button("Home 🏠"):
        selected_option.write(f"Selected: {options[0]}")
    if menu_col2.button("Upload 📤"):
        selected_option.write(f"Selected: {options[1]}")
    if menu_col3.button("Tasks 📝"):
        selected_option.write(f"Selected: {options[2]}")
    if menu_col4.button("Settings ⚙️"):
        selected_option.write(f"Selected: {options[3]}")

if __name__ == "__main__":
    main()


