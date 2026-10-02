import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df=pd.read_csv("data.csv")

type_count=df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index, type_count.values)

plt.show()