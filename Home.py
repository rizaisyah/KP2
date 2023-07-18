import streamlit as st

def main():
    st.title("My Streamlit App")

    # Menu options
    options = ["Home 🏠", "Upload 📤", "Tasks 📝", "Settings ⚙️"]

    # Display the selected item
    selected_option = st.radio("Select an option:", options, index=0, format_func=lambda x: x.split(' ')[0])

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
                cursor: pointer;
            }
        </style>
    """, unsafe_allow_html=True)

    # Create a horizontal menu bar
    with st.container():
        selected_option.write(f"Selected: {selected_option}")

        if selected_option == "Home 🏠":
            st.write("Welcome to the Home Page!")
        elif selected_option == "Upload 📤":
            st.write("You can upload your files here.")
        elif selected_option == "Tasks 📝":
            st.write("These are your pending tasks.")
        elif selected_option == "Settings ⚙️":
            st.write("Adjust your settings here.")

if __name__ == "__main__":
    main()
