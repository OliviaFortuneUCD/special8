import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
fig,ax = plt.subplots()
plt.show()
data= pd.read_csv("GBvideos.csv")
sns.lineplot(x=data['video_id'].head(5),
y=data['views'].head(5))