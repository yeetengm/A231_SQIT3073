
import pandas as pd
import numpy as np


data = {'Name': ['Yee Teng','Kai Jie','Mark'],
        'Age': [23,23,24],
        'Country':['Msia','Msia','Canada']}

df=pd.DataFrame(data,columns=['Name','Age','Country'])

print('\nList of Names')
print(df)


#2 Input excel data

df=pd.read_csv('/Users/yeetengm/Downloads/hies_2019.csv')
print('\n')
print(df)

