import streamlit as st
import matplotlib.pyplot as plt

# Class to generate multiple Streamlit pages using an object oriented approach
class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon="🍃")

    def add_page(self, title, func) -> None:
        self.pages.append({"title": title, "function": func})

    def run(self):
        """
        Runs the app and displays the selected page.

        The method displays the app title,
        shows a sidebar with the available pages,
        and calls the function of the selected page to display its content.
        """
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()