import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
daft = pd.read_csv('daft_v_2.csv')
print(daft.head(5))




mostexpensive = daft.head()

print(mostexpensive)

# count plot on two categorical variable
sns.countplot(x='price', hue="address", data=mostexpensive)


# Show the plot
plt.show()