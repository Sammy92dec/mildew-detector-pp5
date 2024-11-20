import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict, resize_input_image, plot_predictions_probabilities
)

def page_powdery_mildew_detector_body():
    """
    Displays a Streamlit interface for users to upload images
    of cherry leaves and runs predictions to determine whether
    the leaf is healthy or infected with powdery mildew.
    A downloadable report of the results is provided after analysis.
    """

    st.info(
        f"Upload pictures of cherry leaves to determine whether the leaf is"
        f" healthy or infected with powdery mildew."
        f" A report of the examined leaves will be available for download."
    )

    st.write(
        "*You can download a set of infected and healthy leaves for live prediction from"
        "[here](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).*"
    )

    st.write("---")

    st.write("**Upload a clear picture of a cherry leaf. You may select more than one.**")

    images_buffer = st.file_uploader(' ', type='jpeg', accept_multiple_files=True)

    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:
            img_pil = (Image.open(image))
            st.info(f"Cherry leaf Sample: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(
                img_pil,
                caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height"
                )
            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            df_report = df_report.append({"Name":image.name, 'Result': pred_class},
                                         ignore_index=True)

        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)

    st.write(
         f" For additional information, please visit the "
         f" [Project README file](https://github.com/Sammy92dec/mildew-detector-pp5/blob/main/README.md).")