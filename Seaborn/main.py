import seaborn as sns
import numpy as np
import pandas as pd

#print(sns.get_dataset_names())

penguins=sns.load_dataset('penguins')
'''print(penguins.head())

print(penguins["species"].value_counts())
print(penguins["island"].value_counts())
'''
df=pd.DataFrame(penguins)
df.fillna('Nan', inplace=True)
print(df)
