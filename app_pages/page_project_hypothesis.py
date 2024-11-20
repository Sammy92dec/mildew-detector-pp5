import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* Hypothesis: The machine learning model can accurately predict with the use of images"
        f" whether a cherry leaf is healthy or contains powdery mildew based on its features.\n\n"
        f"* Validation: By following a systematic approach that includes data preparation,"
        f" model training, and evaluation of healthy cherry leaves images and those that "
        f" contain powdery mildew.\n\n"
        f"Cherry leaves containing powdery mildew can be distinguished from healthy leaves by "
        f" their appearance. This is verified by creating an average image study and an image "
        f" montage to determine the differences in the appearance of both contaminated leave "
        f" and healthy leaves.\n\n"
        f"Contaminated leaves and healthy leaves can be determined with a 97% accuracy,"
        f" this is verified by evaluating the model on the test dataset, which achieve"
        f" above the required accuracy of 97%.")
    
    st.write(
        f" For additional information, please visit the "
        f" [Project README file](https://github.com/Sammy92dec/mildew-detector-pp5/blob/main/README.md).")