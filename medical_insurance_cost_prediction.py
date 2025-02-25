

# **Importing the Dependencies**

Importing dependencies in a machine learning project involves including essential libraries and frameworks required for data manipulation, modeling, and evaluation.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# We are loading the data from csv file to a Pandas DataFrame
insurance_dataset = pd.read_csv('/content/insurance.csv')

# Now Let's load first 5 rows of the dataframe
insurance_dataset.head()

# Number of rows and columns in our dataset
insurance_dataset.shape

# Getting some informations about the dataset
insurance_dataset.info()

"""# **List of Categorical Features**


1. Sex
2. Smoker
3. Region  


"""

# Now we are checking for missing valuees
insurance_dataset.isnull().sum()

# Statistical Measures of the dataset
insurance_dataset.describe()

# Distribution of age value
sns.set()
plt.figure(figsize=(6,6))
sns.distplot(insurance_dataset['age'],color='skyblue')
plt.title('Age Distribution')
plt.show()

# Gender column
plt.figure(figsize=(6,6))
sns.countplot(x='sex', data=insurance_dataset,palette='Set1')
plt.title('Sex Distribution')
plt.show()

insurance_dataset['sex'].value_counts()

# Bmi distribution
plt.figure(figsize=(6,6))
sns.distplot(insurance_dataset['bmi'],color='salmon')
plt.title('BMI Distribution')
plt.show()

"""Normal BMI Range --> 18.5 to 24.9"""

# Children column
plt.figure(figsize=(6,6))
sns.countplot(x='children', data=insurance_dataset,palette='rainbow')
plt.title('Children')
plt.show()

insurance_dataset['children'].value_counts()

# Smoker column
plt.figure(figsize=(6,6))
sns.countplot(x='smoker', data=insurance_dataset,palette='rainbow')
plt.title('smoker')
plt.show()

insurance_dataset['smoker'].value_counts()

# region column
plt.figure(figsize=(6,6))
sns.countplot(x='region', data=insurance_dataset,palette='rainbow')
plt.title('region')
plt.show()

insurance_dataset['region'].value_counts()

# Distribution of charges value
plt.figure(figsize=(6,6))
sns.distplot(insurance_dataset['charges'])
plt.title('Charges Distribution')
plt.show()

"""# **Data Pre-Processing**

Data preprocessing is a vital step in preparing data for machine learning models, ensuring it is clean, consistent, and suitable for analysis. It involves handling missing values through imputation or removal, encoding categorical variables into numerical formats, and normalizing or scaling features to standardize their ranges. Additionally, the dataset is typically split into training and testing sets to evaluate model performance. Outliers are addressed, and feature selection techniques are applied to focus on the most relevant variables, ultimately improving the efficiency and accuracy of the model.

Encoding the categorical features
"""

# Encoding sex column
insurance_dataset.replace({'sex':{'male':0,'female':1}}, inplace=True)

# Encoding 'smoker' column
insurance_dataset.replace({'smoker':{'yes':0,'no':1}}, inplace=True)

# Encoding 'region' column
insurance_dataset.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}}, inplace=True)

"""Splitting the Features and Target"""

X = insurance_dataset.drop(columns='charges', axis=1)
Y = insurance_dataset['charges']
print(X)

print(Y)

"""Splitting the data into Training data & Testing Data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""# **Model Training**

Model training is the process of teaching a machine learning model to identify patterns in data by optimizing its parameters using a training dataset. The model learns by minimizing a loss function, which measures the error between predicted and actual values. This step ensures the model generalizes well to unseen data, making accurate predictions.

Linear Regression
"""

# Loading the Linear Regression model
regressor = LinearRegression()

regressor.fit(X_train, Y_train)

"""# **Model Evaluation**

Model evaluation assesses the performance of a trained machine learning model using metrics like accuracy, precision, recall, F1-score, or mean squared error. This step involves testing the model on a separate validation or test dataset to ensure it generalizes well to unseen data. Proper evaluation helps identify overfitting, underfitting, and areas for improvement.
"""

# Prediction on training data
training_data_prediction =regressor.predict(X_train)

# R squared value
r2_train = metrics.r2_score(Y_train, training_data_prediction)
print('R squared vale : ', r2_train)

# Prediction on test data
test_data_prediction =regressor.predict(X_test)

# R squared value
r2_test = metrics.r2_score(Y_test, test_data_prediction)
print('R squared vale : ', r2_test)

"""# **Building a Predictive System**

Building a predictive model involves selecting an appropriate algorithm based on the problem type (e.g., regression or classification) and training it using historical data. The model learns patterns from the input features to predict future or unseen outcomes. Once trained, the model is evaluated for accuracy and fine-tuned through hyperparameter optimization to improve its performance and reliability.
"""

# input_data =(Age,Sex,BMI,No of Children,Smoker,Region)
# Numeric Notation For categorical features:
# Sex (Male=0, Female=1)
# Smoker(Yes=0, No=1)
# Region(SouthEast=0 , SouthWest=1 , NorthEast=2 , NorthWest=3)
input_data = (22,0,25.74,3,0,0)

# changing input_data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = regressor.predict(input_data_reshaped)
print(prediction)

print('The insurance cost in USD is ', prediction[0])
