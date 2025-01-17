import pandas as pd

attrition_data = pd.read_csv("HR-Employee-Attrition.csv")


#Load Data

print("Load Data : \n *****************************")
print(attrition_data.head(5))

#Shape
print("Dataset Shape : \n *****************************")

print(attrition_data.shape)

#Size
print("Dataset Size : \n *****************************")

print(attrition_data.size)

#Information
print("Dataset Information  : \n *****************************")

print(attrition_data.info())

#Check For Null Values
print("Check Null Values : \n *****************************")
print(attrition_data.isnull().sum())

#Check for Duplicate Values
print("Check Duplicate Values : \n *****************************")
print(attrition_data.duplicated().sum())



 ''' EDA '''  

print("Check Numerical Values Description : \n *****************************")
print(attrition_data.describe())


