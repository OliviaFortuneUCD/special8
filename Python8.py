import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
daft = pd.read_csv('daft_v_2.csv')
print(daft.head(5))




mostcheapest = daft.tail()

print(mostcheapest)

# count plot on two categorical variable
sns.countplot(x='price', hue="address", data=mostcheapest)


# Show the plot
plt.show()