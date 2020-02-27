##Import libraries
import pandas as pd
import numpy as np

##Import data
data = pd.read_excel("dog data.xlsx")

##Drop rows with any missing values
data = data.dropna()


##Change column names
data.columns.values[4] = "Age(years)"
print(data.columns.ravel())

print(data)