import streamlit as st


def main():
    # Base64-encoded representation of the 🦸‍♂️ emoji
    icon_base64 = "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADbSURBVDhPtZIxDoBACMRcJ/u+A2MBuSbcRmKkFzBLA0mCQ3BFwHLLl58AybwC8Odw7G0j0FCopVSaKBN5zgwaTWAMo1sLMTMzn7/pQQTEdQ9AyBskOhp7IB0Aj8gM1S5XxFyZoAAAAASUVORK5CYII="

    # Custom HTML to add the icon to the Streamlit app's tab in Streamlit Cloud
    st.markdown(
        f"""
        <head>
            <link rel="icon" href="data:image/png;base64,{icon_base64}">
        </head>
        """,
        unsafe_allow_html=True
    )

    # Your Streamlit app content here
    st.title("Welcome to My Streamlit App")
    st.write("This is the main page content.")

if __name__ == "__main__":
    main()


