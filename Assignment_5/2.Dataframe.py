import pandas as pd

#creation of dataframe using list
data = [
    ['Bhumi', 19, 'India'],
    ['Mahak', 20, 'London'],
    ['Chetan', 21, 'China']
]
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)

#creation of dataframe using dictionary
data_set={'Fruits':["apple","mango","banana"],
          'Quantity':[3,10,7]}
var=pd.DataFrame(data_set)
print(var)
print(type(var))

#creation of dataframe using list of list
lili=[['1','Rohan'],
      ['2','sohan']]
le=pd.DataFrame(lili,columns=['Id','Name'])
print(le)


#creation of dataframe using list of dictionary
lists=[{'Name':'Bhumi','Age':20,'Branch':'CSE'},
       {'Name':'Anushri','Age':19,'Branch':'IT'},
       {'Name':'Sanskriti','Age':20,'Branch':'IOT'}
       ]
li=pd.DataFrame(lists)
print(li)
print(type(li))


#creation of dataframe using list of tuples
tup=[('Cup',2,'220'),
     ('Glass','4','370')]
tu=pd.DataFrame(tup,columns=['Items','Quantity','Prize'])
print(tu)