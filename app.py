import streamlit as st
from app_pages.multipage import MultiPage

# Ensure this is the first Streamlit command
st.set_page_config(
    page_title="Mildew Detection - Cherry Leaves",
    layout="wide"
)

# Continue with your app setup
from app_pages.page_summary import page_summary_body
from app_pages.page_cherry_leaves_visualizer import page_cherry_leaves_visualizer_body
from app_pages.page_powdery_mildew_detection import page_powdery_mildew_detection_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_metrics

app = MultiPage(app_name="Mildew Detection - Cherry Leaves")
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Cherry Leaves Visualiser", page_cherry_leaves_visualizer_body)
app.add_page("Powdery Mildew detection", page_powdery_mildew_detection_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("ML Performance Metrics", page_ml_performance_metrics)
app.run()