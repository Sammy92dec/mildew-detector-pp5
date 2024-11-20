import streamlit as st
from app_pages.multipage import MultiPage

# loads the pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_cherry_leaves_visualizer import page_cherry_leaves_visualizer_body
from app_pages.page_powdery_mildew_detection import page_powdery_mildew_detection_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_metrics

app = MultiPage(app_name="Mildew Detection - Cherry Leaves")  # Creates an instance of the app

# app pages are added here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Leaves Visualiser", page_cherry_leaves_visualizer_body)
app.add_page("Mildew Detector", page_powdery_mildew_detection_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("ML Performance Metrics", page_ml_performance_metrics)

app.run()