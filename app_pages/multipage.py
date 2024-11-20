import streamlit as st
import matplotlib.pyplot as plt


class MultiPage:
    """Framework for managing multiple Streamlit pages."""
    
    def __init__(self, app_name):
        self.pages = []
        self.app_name = app_name

    def add_page(self, title, func):
        """Add a new page to the app."""
        self.pages.append({"title": title, "function": func})

    def run(self):
        # Render the sidebar with a dropdown to select the page
        st.sidebar.title(self.app_name)
        page = st.sidebar.selectbox(
            "Navigate to:",
            self.pages,
            format_func=lambda page: page["title"]
        )

        # Run the selected page's function
        page["function"]()