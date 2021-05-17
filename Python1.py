# Import the libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
titanic = sns.load_dataset("titanic")

# Set up a factorplot
g = sns.factorplot("class", "survived", "sex", data=titanic, kind="bar", size=6, aspect=2, palette="muted", legend=False)

# Show plot
plt.show()