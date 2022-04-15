import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.cluster import KMeans

#Loading the data about Mall Customers into a Pandas Dataframe. 
customer_data = pd.read_csv('Mall_Customers.csv')

#Now let's take a look at the first few rows to understand the data better
customer_data.head()
#We can also look at how many rows and columns are present in the data
#and get some more info about the dataset we are using
customer_data.shape
customer_data.info()


#Checking for missing values in the dataset
customer_data.isnull().sum()
