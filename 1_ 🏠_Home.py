import streamlit as st

def page_home():
    st.title('Home Page')
    # Your home page content here

def page_about():
    st.title('About Page')
    # Your about page content here

def page_contact():
    st.title('Contact Page')
    # Your contact page content here

def main():
    st.sidebar.title('Navigation')
    pages = {
        'Home': page_home,
        'About': page_about,
        'Contact': page_contact
    }

    selection = st.sidebar.radio("Go to", list(pages.keys()))

    # Run the selected page
    pages[selection]()

if __name__ == '__main__':
    main()
