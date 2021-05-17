import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('Hotel.csv')

# Truncate
df = df[['arrival_date_year', 'arrival_date_month', 'stays_in_week_nights']]
# Save the order of the arrival months
order = df['arrival_date_month']
# Pivot the table to turn it into wide-form
df_wide = df.pivot_table(index='arrival_date_month', columns='arrival_date_year', values='stays_in_week_nights')
# Reindex the DataFrame with the `order` variable to keep the same order of months as before
df_wide = df_wide.reindex(order, axis=0)

print(df_wide)
sns.lineplot(data=df_wide)
plt.show()