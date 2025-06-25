import pandas as pd

df1=pd.DataFrame({"Id":[1,2,3],
                  "Name":['Bhumi','Chetan','Sanskriti'],
                  'Branch':['CS','CS','IOT']
                  })

df2=pd.DataFrame({"Id":[1,2,3],
                  "Name":['Mahak','Ishani','Anushri'],
                  'Branch':['IT','CS','IT']
                  })
df=df1.merge(df2,on='Id')
print("Merging:\n",df)
left_merge=df1.merge(df2,on='Id',how='left')
print("Left join:\n",left_merge)
right_merge=df1.merge(df2,on='Id',how='right')
print("Right Join:\n",right_merge)


#if there is any missing values then in resulting dataframe
#there is a value "NAN" will appear on that position
df1_index=df1.set_index('Id')
df2_index=df2.set_index('Id')

index_join=df1_index.join(df2_index,lsuffix='_l',rsuffix='-r')
print("Index_Based_Join:\n",index_join)


#merging using multiple keys
le_merge=df1.merge(df2,on=['Id','Branch'])
print(le_merge)

le_mge=df1.merge(df2,on=['Id','Branch'],how="outer")
print(le_mge)

right_join = pd.merge(df1, df2, on='Id', how='right')
print("Right Join:\n", right_join)

#if we need to obtain the output from outer keys than we need to set_index="Other_key"
df=df1.join(df2,on='Id',rsuffix='_r',lsuffix='_l')
print("Join:\n",df)