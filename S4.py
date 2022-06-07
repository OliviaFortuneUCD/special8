import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from matplotlib import style
netflix_data = pd.read_csv("GBvideos.csv")
print(netflix_data.head())
# how much repeat the company ?

plt.figure(figsize=(10,7))
sns.countplot(netflix_data["category_id"])

