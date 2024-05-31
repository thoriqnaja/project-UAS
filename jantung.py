import warnings
import os

import numpy as np  # NumPy for numerical computing
import pandas as pd  # Pandas for data manipulation and analysis

# Data visualization libraries
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

warnings.simplefilter(action='ignore', category=Warning)

# Some Pandas settings
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)
df = pd.read_csv("/kaggle/input/d/mexwell/heart-disease-dataset/heart_statlog_cleveland_hungary_final.csv")
def check_df(dataframe):
    print("##################### Row and Column Count #####################")
    print(dataframe.shape)
    print("\n##################### Column Names #####################")
    print(dataframe.columns)
    print("\n##################### First Five Rows #####################")
    print(dataframe.head())
    print("\n##################### Last Five Rows #####################")
    print(dataframe.tail())
    print("\n##################### DataFrame Information #####################")
    dataframe.info()
    print("\n##################### Data Types #####################")
    print(dataframe.dtypes)


check_df(df)
