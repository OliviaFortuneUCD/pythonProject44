import seaborn as sns
sns.set_theme(style="ticks")

df = sns.load_dataset("mpg")
sns.pairplot(df, hue="origin")