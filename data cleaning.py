##Import libraries
import pandas as pd
#import numpy as np

##Import data
data = pd.read_excel("dog data.xlsx")

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None) #displays all columns in single line
pd.set_option('display.max_colwidth', -1) #print contents of columns w/o truncation

print("Original Data")
print(data)
print("--------------------------------------------------")

##Drop rows with any missing values
def drop_function(_axis, dropHow):
   dropped_data = data.dropna(axis = _axis, how = dropHow)
   print("Dropped Data")
   print (dropped_data)
   print("--------------------------------------------------")


drop_function(0, 'all')

##Drop a column
##data = data.drop('Gender', axis=1)

##Change column names
data.columns.values[4] = "Age(years)"

print("Updated Columns Data")
print(data)
print("--------------------------------------------------")