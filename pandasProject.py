import pandas as pd
Data_frame=pd.read_csv('housing.csv')
a=Data_frame
#print(a)                    #to read and get all the dataframe
print('1 >',a.head(6))            #to get starting rows
print('2 >',a.tail(4))            #to get last rows
print('3 >',a[10:20])             #to get particular inBetween rows
print('4 >',a.price.mean())       #to get mean of particular int column values #df['salary'].mean()
print('5 >',a.bedrooms.dtype)                   #series      #prints type of the column
print('6 >',a[['bedrooms','price']])            #data frame  #prints particular columns
print('7 >',a.groupby('bedrooms')[['price']].mean())
print('8 >',a[a['price']<25000])
print('9 >',a.describe())
