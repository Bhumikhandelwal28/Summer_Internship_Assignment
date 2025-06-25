import pandas as pd
dfA = pd.DataFrame({'ID': [1, 2], 'Score': [80, 90]})
dfB = pd.DataFrame({'ID': [3, 4], 'Score': [85, 75]})
dfC = pd.DataFrame({'ID': [2, 3, 4], 'Grade': ['A', 'B', 'C']})

# Concatenate vertically
concat_df = pd.concat([dfA, dfB], ignore_index=True)
print("Concatenate dataframes:\n",concat_df)
# Merge concat_df with dfC on 'ID'
final_df = pd.merge(concat_df, dfC, on='ID', how='left')
print("Final Merged DataFrame:\n", final_df)

fi_df=concat_df.join(dfC,on="ID",how='left',lsuffix="_l",rsuffix='_r')
print(fi_df)
