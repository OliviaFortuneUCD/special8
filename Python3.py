# importing required libraries
import seaborn as sns
sns.set()
sns.set(style="darkgrid")



import numpy as np
import pandas as pd

# importing matplotlib
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
plt.rcParams['figure.figsize']=(10,10)

data_BM = pd.read_csv('train_v9rqX0R.csv')
# drop the null values
data_BM = data_BM.dropna(how="any")
data_BM["Visibility_Scaled"] = data_BM["Item_Visibility"] * 100
# view the top results

sns.barplot(x="Item_Type", y="Item_MRP", data=data_BM[:5])
plt.show()