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
#Axis0 = row Axis1 = Column
def drop_na (_axis, dropHow):
   dropped_data = data.dropna(axis = _axis, how = dropHow)
   print("Dropped Data")
   print (dropped_data)
   print("--------------------------------------------------")

##Drop a column by Column Index (starts at 0)
#dop func -> data.drop('Gender', axis=1)
def drop_col (index):
    drop_col_data = data.drop(data.columns[index], axis = 1)
    print("Dropped Column Data")
    print (drop_col_data)
    print("--------------------------------------------------")   
    
##Change column names
#data.columns.values[4] = "Age(years)"
def col_name (index, newName):
    temp_Data = data.copy()
    temp_Data.columns.values[index] = newName
    print("Updated Columns")
    print(temp_Data)
    print("--------------------------------------------------")





#  col_name(4, 'Age') Index to modify & NewName
    
#  drop_col(2) Index to drop
    
#  drop_na(0, 'all') Axis and HowtoDrop


##Add Input Feature
#data=pd.read_exce;("dog data.xlsx")
input_feature = input("Enter Dog's Name")
print(input_feature)
