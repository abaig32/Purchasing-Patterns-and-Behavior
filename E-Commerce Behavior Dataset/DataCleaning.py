import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from KMeans import CustomKMeans
import os
from sklearn.cluster import KMeans



def clean_data(dataset):
    # Load the dataset
    df = pd.read_csv(dataset)

    # Display all columns
    pd.set_option('display.max_columns', None)

    # #Analyzing the dataset
    df.info()

    #Dropping Duplicate Rows
    df.drop_duplicates(inplace=True)


    #Detecting Missing Values
    print(df.isnull().sum())



    #Dropping all the null values
    df = df.dropna()

    return df