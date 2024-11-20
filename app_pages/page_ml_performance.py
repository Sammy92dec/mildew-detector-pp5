import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics():
    """
    Displays a summary of the dataset's distribution,
    the model's performance metrics,
    and a detailed explanation of the results.
    It includes visualisations such as pie charts,
    classification reports, ROC curves, and confusion matrices.
    """
    version = 'v1'
    st.info(
        f"This page presents an easy-to-understand summary of the"
        f" dataset's division, the model's performance on it, and"
        f" a concise explanation of the outcomes."
    )

    st.write("### Images Distribution per Set & Label ")

    labels_distribution = plt.imread(f"outputs/v1/number_leaves_sets.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')

    # Display the image showing the overall sets distribution
    labels_distribution = plt.imread(f"outputs/{version}/sets_distribution_bar.png")
    st.image(labels_distribution, caption='Sets Distribution')

    st.warning(
        f"The cherry leaves dataset was divided into three subsets:\n\n"
        f"A training set (70% of the data) to train the model and"
        f" create an initial baseline for generalization and prediction.\n\n"
        f"A validation set (10% of the data) to adjust the"
        f" model after each epoch\n\n"
        f"A test set (20% of the data) to assess the model"
        f" accuracy after the training phase.")
    st.write("---")

    st.write("### Model Performance")

    # Display the classification report image
    model_clf = plt.imread(f"outputs/{version}/clf_report.png")
    st.image(model_clf, caption='Classification Report')

    st.warning(
        f"**Classification Report**\n\n"
        f"Precision: Percentage of correct predictions.\n\n"
        f"Recall: Percentage of positive cases detected.\n\n"
        f"F1 Score: Percentage of correct positive predictions.\n\n"
        f"Support: Number of occurrences of a particular"
        f" class in a selected dataset.")

    # Display the ROC curve image
    model_roc = plt.imread(f"outputs/{version}/roccurve.png")
    st.image(model_roc, caption='ROC Curve')

    st.warning(
        f"**ROC Curve**\n\n"
        f"ROC curve is a graphical representation used to evaluate"
        f" the performance of a binary classification model."
        f"It plots the True Positive Rate (sensitivity) against the"
        f" False Positive Rate (1 - specificity)"
        f" at various threshold settings. The ROC curve helps visualise"
        f" how well a model distinguishes between two classes.\n\n"
        f"A model with a curve that rises quickly towards the top-left"
        f" corner of the graph is considered to have good performance,"
        f" indicating high true positive rates with low false positive rates.")

    # Display the confusion matrix image
    model_cm = plt.imread(f"outputs/{version}/confusion_matrix.png")
    st.image(model_cm, caption='Confusion Matrix')

    st.warning(
        f"**Confusion Matrix**\n\n"
        f"A confusion matrix is a table used to evaluate the performance"
        f" of a classification model by comparing its predictions with"
        f" the actual outcomes.\n\n"
        f"True Positive: The number of correct predictions where the"
        f" model correctly identifies the positive class.\n\n"
        f"True Negative: The number of correct predictions where the"
        f" model correctly identifies the negative class.\n\n"
        f"False Positive: The number of incorrect predictions where"
        f" the model incorrectly identifies the negative class as"
        f" positive (also known as Type I error).\n\n"
        f"False Negative: The number of incorrect predictions where"
        f" the model incorrectly identifies the positive class as"
        f" negative (also known as Type II error).\n\n"
        f"High TP and TN rates, with low FP and FN rates"
        f" are indicative of a good model.")

    # Display the model performance image
    model_perf = plt.imread(f"outputs/{version}/model_history.png")
    st.image(model_perf, caption='Model Performance')

    st.warning(
        f"**Model Performance**\n\n"
        f"Model performance in machine learning refers to how well a"
        f" model makes predictions or classifications based on"
        f" the input data.\n\n"
        f"It is typically evaluated using metrics such as accuracy,"
        f" precision, recall, F1 score, and area under the ROC curve,"
        f" depending on the type of problem being solved.\n\n"
        f"High performance indicates that the model accurately captures"
        f" patterns in the data and generalizes well to new, unseen data.\n\n"
        f"Poor performance suggests that the model may be overfitting"
        f" to the training data or underfitting, meaning it is too simple"
        f" to capture the underlying patterns.\n\n"
        f"Val_loss (Validation Loss): Validation loss measures the error"
        f" of the model's predictions on the validation set.\n\n"
        f"Accuracy: Accuracy is the ratio of correctly predicted"
        f" instances to the total instances in the dataset. It is a"
        f" measure of how well the model's predictions match the actual"
        f" labels in the dataset.\n\n"
        f"Val_acc (Validation Accuracy): Validation accuracy measures the"
        f" proportion of correct predictions made by the model on the"
        f" validation set, which is separate from the training data."
        f" This metric helps in understanding how well the model is"
        f" generalizing beyond the training data.\n\n"
        f"Monitoring and improving model performance is crucial for"
        f" deploying reliable and effective machine learning solutions.")

    st.write("### Generalised Performance on Test Set")

    # Display the model's performance on the test set using a dataframe
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))
    
st.write(
        f" For additional information, please visit the "
        f" [Project README file](https://github.com/Sammy92dec/mildew-detector-pp5/blob/main/README.md).")