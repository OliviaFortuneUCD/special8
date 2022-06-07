import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
daft = pd.read_csv('daft_v_2.csv')


Ballymun= (daft[daft['address'].str.contains('Ballymun')])
Swords= (daft[daft['address'].str.contains('Swords')])
frames = [Ballymun, Swords]

result = pd.concat(frames)

#
sns.relplot(x="bathroom", y="price", hue="bedroom" ,
            sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=result)