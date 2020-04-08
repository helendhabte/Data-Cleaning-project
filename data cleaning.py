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


##Input Example
#data=pd.read_exce;("dog data.xlsx")
#input_feature = input("Enter Dog's Name:")
#print(input_feature)

##Drop rows with any missing values (NA or empty cells)
#Axis0 = row / Axis1 = Column
#dropHow = "any" or "all"
def drop_na (_axis, dropHow):
    drop_na_data = data.dropna(axis = _axis, how = dropHow)
    print("Dropped Empty Data")
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
    
##Modify Single Cell
def cell_value (row, column, newData):
    temp_Data2 = data.copy()
    temp_Data2.iat[row, column] = newData
    print("Modified Cell")
    print(temp_Data2)

##Welcome message & instructions  
user_input = input("Welcome to the Data Cleaning Tool. Choose [1] Drop empty rows/columns [2] Drop Column [3] Drop Row [4] Change Column Name [5] Modify Single Cell: ")

if int(user_input) == 1:
    param_input1 = input("Remove row(0) or column(1)? ")
    param_input2 = input("Drop cells with all or any missing values? ")
    drop_na (int(param_input1), param_input2)
    print("Data Dropped")
    
elif int(user_input) == 2:
    col_index = input("Enter the column index to drop: ")
    drop_col(int(col_index))
    print("Column Dropped")

elif int(user_input) == 3:
    row_index = input("Enter the row index to drop: ")
    drop_row(int(row_index))
    print("Row Dropped")

elif int(user_input) == 4:
    input1 = input("Enter column index to modify: ")
    input2 = input("Enter new column name: ")
    col_name(int(input1), input2)
    print("Column Modified")

elif int(user_input) == 5:
    row_input = input("Row to modify: ")
    col_input = input("Column to modify: ")
    newData_input = input("Input new data: ")
    cell_value(int(row_input), int(col_input), newData_input)
    print("Cell Modified")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  