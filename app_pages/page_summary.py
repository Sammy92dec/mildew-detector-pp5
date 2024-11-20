import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():
    """
    Displays a summary of the project, including general information about
    cherry powdery mildew, details on the dataset, and business requirements.
    """
    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n\n"
        f"Cherry powdery mildew is a fungal disease caused by the pathogen "
        f"Podosphaera clandestina, which primarily affects cherry trees. "
        f"Infected plants display white to grayish powdery spots, which are "
        f"the fungal spores and mycelia. However, as the infection progresses,"
        f" these spots can merge, covering large areas of leaf surface.\n\n"
        f"This disease thrives in warm, dry conditions & can spread rapidly, "
        f"especially in humid environments.\n\n"
        f"It typically infects the young leaves, shoots, and fruit of cherry "
        f"trees, resulting in reduced fruit quality and yield.\n\n"
        f"The mildew fungus lives on the surface of plant tissues & feeds on "
        f"them by sending tiny filaments into the cells.\n\n"
        f"Several leaves, infected and healthy, were picked and examined.\n\n"
        f"Visual criteria used to detect infected leaves are:\n\n"
        f"* Porraceous green lesions on either leaf surface\n"
        f"* White or grayish powdery spots which develop in the infected area "
        f"on leaves and fruits."
    )

    st.success(
        f"The project has three business requirements:\n\n"
        f"1 - A comprehensive study to visually differentiate between healthy "
        f"cherry leaves and those infected with powdery mildew.\n\n"
        f"2 - Implement a predictive model capable of identifying whether a "
        f"cherry leaf is healthy or contains powdery mildew based on image "
        f"analysis, ideally with an accuracy target of not less than 97%.\n\n"
        f"3 - Develop an interactive dashboard that allows users to upload "
        f"cherry leaf images, receive predictions, and review the analysis "
        f"results."
    )

    st.warning(
        f"**Project Dataset**\n\n"
        f"The available dataset contains  healthy leaves &  affected "
        f"leaves, individually photographed against a neutral background."
    )

    st.write(
        f"For additional information, please visit "
        f"[Project README file](https://github.com/Sammy92dec/mildew-detector-pp5/"
        f"blob/main/README.md)."
    )