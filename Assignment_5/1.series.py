import pandas as pd

#creation of pandas series using dictionary
data={'Fruit':'Apple','Color':'Red','Taste':'Sweet'}
da=pd.Series(data)
print(da)

#accessing series
print(da['Color'])
print(da.iloc[1])

#creation of pandas series using lists
lis=['Apple','Mango','Banana']
li=pd.Series(lis,index=['1','2','3'])
print(li)

#accessing series
print(li.iloc[1])
print(li.loc['2'])

#conversion of Series into list
print(da.tolist())