import streamlit as st

def main():
    st.title("My Streamlit App")

    # Menu options
    options = ["Home 🏠", "Upload 📤", "Tasks 📝", "Settings ⚙️"]
    selected_option = st.radio("", options, format_func=lambda x: x.split(' ')[0], key='menu')

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

    # Display content based on the selected option
    if "Home" in selected_option:
        st.write("Welcome to the Home Page!")
    elif "Upload" in selected_option:
        st.write("You can upload your files here.")
    elif "Tasks" in selected_option:
        st.write("These are your pending tasks.")
    elif "Settings" in selected_option:
        st.write("Adjust your settings here.")

    # Make the layout horizontal using beta_columns
    cols = st.beta_columns(len(options))
    for col, option in zip(cols, options):
        col.write(option)

if __name__ == "__main__":
    main()
