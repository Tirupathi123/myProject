import pandas as pd
Data_frame=pd.read_csv('housing.csv')
a=Data_frame
print(a)                    #to read and get all the dataframe
print(a.head(6))            #to get starting rows
print(a.tail(4))            #to get last rows
print(a[10:20])             #to get particular inBetween rows
print(a.price.mean())       #to get mean of particular int column values #df['salary'].mean()
print(a.bedrooms.dtype)                   #series      #prints type of the column
print(a[['bedrooms','price']])            #data frame  #prints particular columns
print(a.groupby('lotsize')[['price']].mean())
print(a[a['price']<30000])
print(a.dropna())
print(a.describe())
