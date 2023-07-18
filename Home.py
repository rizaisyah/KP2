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
                padding: 10px 0;
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
        st.write("", options[0], key='home')
        st.write("", options[1], key='upload')
        st.write("", options[2], key='tasks')
        st.write("", options[3], key='settings')

    # Handle button clicks
    if st.button(options[0], key='Home'):
        selected_option.write(f"Selected: {options[0]}")
    if st.button(options[1], key='Upload'):
        selected_option.write(f"Selected: {options[1]}")
    if st.button(options[2], key='Tasks'):
        selected_option.write(f"Selected: {options[2]}")
    if st.button(options[3], key='Settings'):
        selected_option.write(f"Selected: {options[3]}")

if __name__ == "__main__":
    main()


