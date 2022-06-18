import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dython.nominal import associations
import seaborn as sns


#from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier

#seed
np.random.seed(42)

# metrics
from sklearn.metrics import classification_report, confusion_matrix , accuracy_score, precision_score, recall_score, f1_score

# tunning
# import hyperparameter tuning with randomizedSearchCV
from sklearn.model_selection import RandomizedSearchCV

# KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier


#***************************************************
st.header("Mazi's predictions")
st.write("##### *This site helps you predict the price of \
your car based on certain features*" )

#***************************************************
st.header("The datasets scraped from website")
st.write("##### *We have built a database of prices for you, \
so the model can predict accurately*" )



Estimator = st.selectbox ("Select Classifier",['Select classifier','RandomForestClassifier'])
def select_estimator(estimator):
    #train = pd.read_csv('train.csv')
    if Estimator == "RandomForestClassifier":
        return 'Imported ..... sklearn.ensemble import RandomForestClassifier'
    else:
        return "none"

st.write(select_estimator(Estimator))


Dataset = st.selectbox ("Select dataset",['Select dataset','Train','Others'])

#from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier


def select_df(df):
    train = pd.read_csv('train.csv')
    if Dataset == "Train":
        return train
    else:
        return "none"

st.write(select_df(Dataset))
