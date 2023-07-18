from st_pages import Page, add_page_title, show_pages

"## Declaring the pages in your app:"

show_pages(
    [
        Page("pages/1_ 🏠_Home.py", "Home", "🏠"),
        # Can use :<icon-name>: or the actual icon
        Page("pages/2_📝_Tutorial.py", "Tutorial", ":books:"),
        # The pages appear in the order you pass them
        Page("pages/3_🔧_Tools.py", "Example Four", "📖"),
        Page("pages/4_🕵️‍♀️_Real-case.py", "Example Two", "✏️"),
        Page("pages/5_📂_Resources.py", "Example Five", "🧰"),
    ]
)

add_page_title()  # Optional method to add title and icon to current page
