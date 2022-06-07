import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
daft = pd.read_csv('daft_v_2.csv')
print(daft.head(5))



sns.set_theme(style="whitegrid")
print(daft.columns)

Ballymun= (daft[daft['address'].str.contains('Ballymun')])





# count plot on two categorical variable
sns.countplot(x='bathroom', hue="address", data=Ballymun)


# Show the plot
plt.show()