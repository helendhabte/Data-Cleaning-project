##Import libraries
import pandas as pd

##Import data
data = pd.read_excel('dog_data.xlsx')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None) #displays all columns in single line
pd.set_option('display.max_colwidth', -1) #print contents of columns w/o truncation

print("Original Data")
print(data)
print("--------------------------------------------------")

##Add Input Feature
#data=pd.read_exce;("dog data.xlsx")
input_feature = input("Enter Dog's Name:")
print(input_feature)

##Drop rows with any missing values
#Axis0 = row 
#Axis1 = Column
def drop_na (_axis, dropHow):
   drop_na_data = data.dropna(axis = _axis, how = dropHow)
   print("Dropped NA Data")
   print (drop_na_data)
   print("--------------------------------------------------")

##Drop a column by Column Index (starts at 0)
#dop func -> data.drop('Gender', axis=1)
def drop_col (index):
    drop_col_data = data.drop(data.columns[index], axis = 1)
    print("Dropped Column Data")
    print (drop_col_data)
    print("--------------------------------------------------")   

##Drop a row by Row Index
#data.drop(data.index[0])
def drop_row (index):
    drop_row_data = data.drop(data.rows[index])
    print("Drop Row Data")
    print(drop_row_data)
    print("--------------------------------------------------") 
    
##Change column name
#data.columns.values[4] = "Age(years)" Index to modify & assign NewName
def col_name (index, newName):
    temp_Data = data.copy()
    temp_Data.columns.values[index] = newName
    print("Updated Columns")
    print(temp_Data)
    print("--------------------------------------------------")
