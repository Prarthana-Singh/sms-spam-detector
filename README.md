 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/prarthanasingh) [![Medium](https://img.shields.io/badge/Medium-12100E?logo=medium&logoColor=white)](https://medium.com/@prarthanasingh) [![X](https://img.shields.io/badge/X-black.svg?logo=X&logoColor=white)](https://x.com/ps3493049) [![kaggle](https://img.shields.io/badge/kaggle-blue.svg?logo=&logoColor=wh)](https://www.kaggle.com/prarthanasinghsengar) 

# SPAM Classifier Project📩 

<br>

## Overview
SMS Spam Detection is a machine learning model that takes an SMS as input and predicts whether the message is a spam or not spam message. The model is built using Python and deployed on the web using Streamlit.

## Introduction
This project aims to develop a text classification model using data science techniques in Python to classify SMS messages as either spam or non-spam.

[![Video](https://cdn-images-1.medium.com/max/876/1*fTPhu7PqgIbnngbWG5zFWA.gif)](https://cdn-images-1.medium.com/max/876/1*fTPhu7PqgIbnngbWG5zFWA.gif)

### Pictures

 **Screen 1** 
 ![Image 1](https://github.com/user-attachments/assets/955aeaa6-7b0a-4656-81ef-b1d624a51386)
<br>
<br>
**Screen 2** 
 ![Image 2](https://github.com/user-attachments/assets/3d17cb1d-0da4-448d-9919-f42145f7c042)
<br>
<br>
**Screen 3** 
 ![Image 3](https://github.com/user-attachments/assets/a5955d97-4b7a-4ba9-b09e-8a3b596187ca)
<br>
<br>
**Screen 4** 
 ![Image 4](https://github.com/user-attachments/assets/9641ca23-fb40-49f1-b44e-6fae6299cfa1)

<br>
<br>


# SMS Spam Classifier using Machine Learning

This project is a robust SMS spam classifier leveraging machine learning techniques to distinguish between spam and non-spam messages. It's designed to provide a reliable solution for identifying unwanted messages, allowing users to filter out potential spam.

## Technology Used
- Python
- Scikit-learn
- Pandas
- NumPy
- Streamlit

## Features
- Data collection
- Data cleaning and preprocessing
- Exploratory Data Analysis
- Model building and selection
- Web deployment using Streamlit

### Data Collection
The SMS Spam Collection dataset was collected from Kaggle, which contains over 5,500 SMS messages labeled as either spam or not spam.
You can access the dataset from [here](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

### Data Cleaning and Preprocessing
The data was cleaned by handling null and duplicate values, and the "type" column was label-encoded. The data was then preprocessed by converting the text into tokens, removing special characters, stop words and punctuation, and stemming the data. The data was also converted to lowercase before preprocessing.

### Exploratory Data Analysis
Exploratory Data Analysis was performed to gain insights into the dataset. The count of characters, words, and sentences was calculated for each message. The correlation between variables was also calculated, and visualizations were created using pyplots, bar charts, pie charts, 5 number summaries, and heatmaps. Word clouds were also created for spam and non-spam messages, and the most frequent words in spam texts were visualized.

### Model Building and Selection
Multiple classifier models were tried, including NaiveBayes, random forest, KNN, decision tree, logistic regression, ExtraTreesClassifier, and SVC. The best classifier was chosen based on precision, with a precision of 100% achieved.

### Web Deployment
The model was deployed on the web using Streamlit. The user interface has a simple input box where the user can input a message, and the model will predict whether it is spam or not spam.

## Demo
To try out the SMS Spam Detection model, visit [here](https://sms-spam-detector-rqf8.onrender.com).

## Usage
To use the SMS Spam Detection model on your own machine, follow these steps:

+ Clone this repository.
+ Install the required Python packages using 
```
pip install -r requirements.txt.
```
+ Run the model using 
```
streamlit run app.py.
```
+ Visit localhost:8501 on your web browser to access the web app.

## License
This project is licensed under the **MIT License**.

---

## Contact
For queries or contributions, feel free to reach out:
- **Author**: Prarthana Singh
- **Email**: prarthanas645@gmail.com
- **GitHub**: [Prarthana-Singh]([https://github.com/siddharth-Kharche](https://github.com/Prarthana-Singh))

