# app.py
from st_pages import Page, show_pages

with st.echo("below"):
    show_pages(
        [
            Page("pages/Home.py", "Home", "🏠"),
            Page("pages/Tutorial.py", "Tutorial", ":books:"),
            Page("pages/Tools.py", "Example Four", "📖"),
            Page("pages/Real-case.py", "Example Two", "✏️"),
            Page("pages/Resources.py", "Example Five", "🧰"),
        ]
    )

