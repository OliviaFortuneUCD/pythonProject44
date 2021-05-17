import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme(style="darkgrid")

df = pd.read_csv('Hotel.csv')

print(df.head(5))