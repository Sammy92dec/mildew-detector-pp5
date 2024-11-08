# Mildew Detection in Cherry Leaves

The goal of this project is to visually differentiate between healthy cherry leaves and those affected by powdery mildew.

Live Link: responsive CHECK

## Table of Contents
1. [Dataset Content](#dataset-content)
2. [Business Requirements](#business-requirements)
3. [Hypothesis and Validation](#hypothesis-and-how-to-validate)
4. [The rationale to map the business requirements](#the-rationale-to-map-the-business-requirements)
5. [ML Business Case](#ml-business-case)
6. [Dashboard Design](#dashboard-design)
7. [Deployment](#deployment)
8. [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
9. [Technologies and Languages Used](#technologies-and-languages-used)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

## Dataset Content

- The dataset used for this project is supplied by Code Institute and sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).
- The dataset contains +4 thousand images taken from the client's crop fields.The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. 
The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

1. The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
2. The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.
3. The client is interested in having the option to download a prediction report for the examined leaves.
4. It was agreed with the client to attain an accuracy rate of 97%.


## Hypothesis and how to validate?

Hypothesis: The machine learning model can accurately predict with the use of images whether a cherry leaf is healthy or contains powdery mildew based on its features

Validation: By following a systematic approach that includes data preparation, model training, and evaluation of healthy cherry leaves images and those that contain powdery mildew. 

Cherry leaves containing powdery mildew can be distinguished from healthy leaves by their appearance. This is verified by creating an average image study and an image montage to determine the differences in the appearance of both contaminated leaves and healthy leaves.
Contaminated leaves and healthy leaves can be determined with a 97% accuracy, this will be verified by evaluating the model on the test dataset, which achieves 99% accuracy.

## The rationale to map the business requirements

### Business Requirement 1: Data Visualisation
- Display the mean and standard deviation images for mildew-infected and uninfected cherry leaves.
- Display the difference between average mildew-infected and uninfected leaves.
- Display an image montage for either mildew-infected or uninfected leaves.
### Business Requirement 2: Classification and Prediction
- Build an ML model and use it to perform predictions based on whether leaves are infected or not, with an accuracy rating of at least 97%.

## ML Business Case

1. Business Objective
    - Objective: By using an ML model we will solve the problem of differentiating between healthy and powdery mildew cherry leaves saving Farmy & Foods many hours of labour used for the current manual process.
    - Business impact: To improve Farmy & Foods crop current health monitoring process, leading to reduced crop losses and maintaining the highest customer satisfaction.
2. Business Problem
    - Description & Challenges: Farmy & Foods is currently spending many hours of manual inspection is time-consuming and prone to errors when trying to identify cherry leaves affected with powdery mildew, leading to ineffective treatments and crop losses.
    - Goals: To make use of an ML model to automatically and accurately identify cherry leaves affected with powdery mildew with at least 97% accuracy.
3. Proposed Solution
    - ML Approach: A Convolutional Neural Network (CNN) model will be developed to classify between healthy and affected with powdery mildew leaf images.
    - Data Requirements: An image data set consisting of images of both healthy and affected with powdery mildew leaves.
4. Business Value
    - By using this model, we expect to quickly and accurately detect affected crops, allowing for early treatments, healthier plants and satisfied customers. Success will be measured by the model's accuracy and how well it works in detecting affected leaves. The benefits will include fewer crop losses and better quality harvests.
5. Risk Mitigation
    - Data Quality: Use strong methods to collect and prepare image data, including adding variety and checking quality, to ensure the dataset is diverse and of high-quality.
    - Model Performance: The model might not reach the required accuracy, so it will be refined by using cross-validation and repeated testing.
    - User: Users might resist the new system. To help, the dashboard withh be user-friendly and simple to use and understand, detailed guides, support, and explanations are available.
    - Data privacy: NDAs and ethical guidelines will be followed to keep cherry leaf images and related data confidential and secure.
6. Implementation Plan
    - Data collection & processing 
    - Model development & training 
    - Model evaluation, testing, optimization and deployment

[Top ⇧](#table-of-contents)

## Dashboard Design

### Page 1 - Project Summary

Page includes some general background on the project, the client, and the reason for the project's inception. 
- The business requirements of the project are stated, as well as details of the dataset.
- The project hypothesis is outlined, linking the business needs with the requirements of the project
- The conclusions of the project are stated, with success measured against the desired business outcomes.

### Page 2 - Leaves Visualiser

This page displays the image plots generated from the DataVisualisation notebook, which answer business requirement 1. Shown are:
- Images displaying the mean and variance for healthy leaves(set 0), and unhealthy leaves(set 1)
- An image showing the visual difference between an average healthy and unhealthy leaf
- An image montage creator, with the option to generate an image montage of either healthy or unhealthy leaves from the dataset

### Page 3 - Mildew Detection

The mildew detection page fulfils business requirement 2, providing the ability for a user to upload images for predicting if mildew is present
- Includes link to dataset for prediction use
- Image upload widget, with the ability to upload multiple image files. These are then standardised and fed into the ML model.
- The images are displayed, with their infection status prediction and probability
- A button allows the user to download a report with prediction details of the images they have uploaded 

### Page 4 - ML Performance

This page summarises the performance metrics of the machine learning model used in the project. Show are:
- A bar graph summarising the data split between the different sets, per label
- Line graphs displaying the accuracy and loss trends for the model
- A summary of the generalised performance of the model on the test data set 

## Unfixed Bugs

- No unfixed bugs were detected 

## Deployment

### Cloning the [GitHub](https://github.com/) repository

Cloning a repository will download a full copy of the data to your computer. This is useful when larger commits need to be pushed, adding or removing files and fixing merge conflicts.

1. Login to GitHub
2. Click the repository you wish to clone (Top left corner)
3. Click 'Code' which is shown above the list of files in the repository
4. Click the 'Local' tab, copy the HTTPS URL
5. Open Gitpod Workspaces, click 'New Workspace'
6. Paste the copied URL into the space given under 'Repository URL'
7. Click 'Continue' and the local clone will be created.

### Forking the [GitHub](https://github.com/) repository

Forking a GitHub repository will allow you to make a copy of the repository, changes can then be made that will not affect the original repository. This is useful for proposed changes, ideas, fixes to an original repository.

1. Login to GitHub
2. Click the repository you wish to fork (Top left corner)
3. Click the 'Fork' drop-down in the top right-hand corner
4. Then click 'Create a new fork' you will now have a copy to work on.

### Heroku

- The App live link is: 

- The project was deployed to Heroku using the following steps.
1. Login to Heroku
2. On the Heroku dashboard click on 'New'
3. Select 'Create New App'
4. Add an app name and select your region
5. Click 'Create App'
6. At the top of the page again, click 'Deploy'
7. Click on 'Github' as your deployment method
8. Search the relevant repo and link these
9. Once linked, select 'Automatic deploys from' or 'Manual Deploy'
10. The deployment process should happen smoothly if all deployment files are fully functional. Click the button 'Open App' on the top of the page to access your App.
11. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Technologies and Languages Used

- [Git & GitHub](https://github.com/)
    - Version control and storage code
- [GitPod](https://www.gitpod.io/) 
    - Used as the development environment
- [Heroku](https://www.heroku.com/) 
    - Used to deploy the site (Cloud based)
- [Am I Responsive](https://ui.dev/amiresponsive) 
    - Used to for the image across devices in the README.md
- [Chat GPT](https://chatgpt.com/) 
    - Used to better word some of my descriptions and general assistance & guidance


## Credits

- Code Institute - Walkthrough Project for steps, guidance and following along to get this far in my project 5:
  - [Code Inst - Malaria Detector](https://shorturl.at/xFj5G)
- Tutor Support for assistance & guidance:
  - [Tutor Assistance](https://learn.codeinstitute.net/ci_support/diplomainfullstacksoftwarecommoncurriculum/tutor)

## Acknowledgements

MY SISTER
[Top ⇧](#table-of-contents)