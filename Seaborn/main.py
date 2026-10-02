import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#print(sns.get_dataset_names())

penguins=sns.load_dataset('penguins')
'''
print(penguins.head())

print(penguins["species"].value_counts())
print(penguins["island"].value_counts())
'''
sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="island")

plt.show()


