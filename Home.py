import streamlit as st

def main():
    with st.sidebar:
        selected = st.radio(
            "Select Page",
            ["Home 🏠", "Learning 🧑‍🏫", "Implementation 👨‍🎨"],
            index=0,
            format_func=lambda page: page.split(' ')[0]
        )

    if "Home" in selected:
        st.title('Home Page')
        # Your home page content here
    elif "Learning" in selected:
        st.title('Learning Page')
        # Your learning page content here
    elif "Implementation" in selected:
        st.title('Implementation Page')
        # Your implementation page content here

if __name__ == "__main__":
    main()

