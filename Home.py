import streamlit as st

def main():
    st.title("My Streamlit App")

    # Menu options
    options = ["Home 🏠", "Upload 📤", "Tasks 📝", "Settings ⚙️"]
    selected_option = st.radio("", options, format_func=lambda x: x.split(' ')[0], key='menu')

    # Display the selected item
    st.write(f"Selected: {selected_option}")

    # CSS styling for the menu bar
    st.markdown("""
        <style>
            .radio span {
                display: inline-flex;
                align-items: center;
            }
            .radio span::before {
                content: "";
                width: 1em;
                height: 1em;
                margin-right: 0.5em;
                display: inline-block;
                border-radius: 50%;
                background-color: #007bff;
                box-shadow: 0 0 0 3px #fff;
            }
        </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

