import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random


def page_leaves_visualiser_body():
    """
    Displays the 'Leaves Visualiser' page,
    providing information on differentiating healthy cherry leaves
    from those infected with powdery mildew.
    It includes options to visualise differences between average
    & variability images,as well as montages of selected labels.
    """
    st.write("### Leaves Visualiser")
    st.info(
        f"A comprehensive study to visually differentiate between"
        f" healthy cherry leaves and those infected with powdery mildew.")

    st.warning(
        f"We believe cherry leaves affected by powdery mildew"
        f" show distinct symptoms.\n\n"
        f" The first symptom is typically a porraceous green,"
        f" circular lesion on leaves and also fruits,"
        f" which progresses to white or grayish powdery spots.\n\n"
        f" In order for the user to apply machine learning functionalities,"
        f" certain modifications & preperations have to be done to images"
        f" prior use of model for optimal feature extraction & training.\n\n"
        f" It is essential to normalise the Image dataset before training"
        f" a Neural Network on it, hence, the mean and standard deviation"
        f" of the entire dataset, that are calculated with a"
        f" mathematical formulawhich takes into consideration"
        f" the properties of an image, are essential."
    )

    version = 'v1'

    if st.checkbox("Difference Between Average & Variability image"):
        """
        Displays the average and variability images of infected and
        healthy leaves if the checkbox is selected.
        It provides a visual comparison between the two.
        """
        avg_powdery_mildew = plt.imread(
            f"outputs/{version}/avg_var_powdery_mildew.png"
            )
        avg_uninfected = plt.imread(f"outputs/{version}/avg_var_healthy.png")

        st.warning(
            f"No significant patterns were identified from the average"
            f" and variability images however, infected leaves"
            f" tended to display more white stipes at the center.")

        st.image(avg_powdery_mildew, caption='Affected Cherry Leaf - Average and Variability')
        st.image(avg_uninfected, caption='Healthy Cherry Leaf - Average and Variability')
        st.write("---")

    if st.checkbox("Differences Between Average Infected & Average Healthy Leaves"):
        """
        Displays the difference between the average
        images of infected and healthy leaves
        if the checkbox is selected.
        """
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        st.warning(
            f"Through the data obtained from this study, we are unable to "
            f" establish patterns to intuitively"
            f" differentiate one from another.")
        st.image(diff_between_avgs, caption='Difference between average images')

    if st.checkbox("Image Montage"):
        """
        Allows the user to select a label and create an image
        montage of the selected label from the validation dataset.
        """
        st.write("To refresh the montage, click on 'Create Montage'")
        my_data_dir = 'inputs/cherryleaves_dataset/cherry-leaves'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(label="Select label", options=labels, index=0)

        if st.button("Create Montage"):
            image_montage(dir_path=my_data_dir + '/validation',
                          label_to_display=label_to_display,
                          nrows=8, ncols=3, figsize=(10,25))
        st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
    """
    Creates and displays a montage of images
    from a specified directory and label.

    Parameters:
    dir_path (str): The path to the directory containing the images.
    label_to_display (str): The label (directory) to display images from.
    nrows (int): Number of rows in the montage.
    ncols (int): Number of columns in the montage.
    figsize (tuple): The size of the figure for the montage.
    """
    sns.set_style("white")
    labels = os.listdir(dir_path)

    if label_to_display in labels:
        images_list = os.listdir(dir_path + '/' + label_to_display)

        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return

        list_rows= range(0, nrows)
        list_cols= range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)

        for x in range(0, nrows*ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()
        st.pyplot(fig=fig)

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")

    st.write(
        f"For additional information, please visit "
        f"[Project README file](https://github.com/Sammy92dec/mildew-detector-pp5/"
        f"blob/main/README.md)."
    )