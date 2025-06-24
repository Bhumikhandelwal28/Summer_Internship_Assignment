import pandas as pd

df = pd.DataFrame({
    'Name': ['Rani', 'Shalini', 'Ishika'],
    'Age': [25, 30, 22]
})

# Select rows with Age > 25
fdf = df[df['Age'] > 25]

print(fdf)

# Select row at index position 1
row = df.iloc[1]
print(row)
Data={'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]}   #here ABC are columns
dt=pd.DataFrame(Data)
print(dt)
col=dt.loc[:,'A']
print(col)

#modify values after slicing
df=pd.DataFrame([['a','b'],['c','d'],['e','f'],['g','h']],columns=["col1","col2"],index=[1,2,3,4])
print(df)
df.iloc[1:3,0]=['x','y']
print(df)
df.loc[1:4,'col1']=['a','b','c','d']
print(df)

#deleting
res=df.drop(2)
print(res)

#deleting rows based on condition
ta=pd.DataFrame({"A":[1,2,3],"B":[4,5,0],"C":[7,8,9]})
print(ta)
result=ta[ta['B']!=0]
print(result)
print(ta)


resu=ta.drop(ta.index[2:4])
print(resu)

print(df.loc[:1, ['Name']])
row_list = df.values.tolist()
print(row_list)


