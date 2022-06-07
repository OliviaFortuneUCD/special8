import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
daft = pd.read_csv('daft_v_2.csv')
print(daft.head(5))



sns.set_theme(style="whitegrid")
print(daft.columns)

Ballymun= (daft[daft['address'].str.contains('Ballymun')])
#Rathmines= (daft[daft['address'].str.contains('Rathmines')])
print(Ballymun['bathroom'])
print (Ballymun['address'])

#
# count plot on single categorical variable
sns.countplot(x='bathroom', data=Ballymun)

# Show the plot
plt.show()