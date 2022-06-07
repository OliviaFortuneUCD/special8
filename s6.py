import seaborn as sns
tips = sns.load_dataset('tips')



#sns.scatterplot(x="total_bill", y="tip", data=tips)

#sns.lineplot(x="size", y="tip",data=tips)

#sns.barplot(x="day", y="tip", data = tips)


#sns.countplot(x='smoker',data=tips)



# Plot miles per gallon against horsepower with other semantics
sns.relplot(x="total_bill", y="tip", hue="smoker", size="size",
            sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=tips)