import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme(style="darkgrid")

df = pd.read_csv('Hotel.csv')

sns.lineplot(x = "arrival_date_month", y = "stays_in_week_nights", data = df)
plt.show()