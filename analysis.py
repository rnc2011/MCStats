import pandas as pd
import matplotlib.pyplot as plt

# Read in the data
df = pd.read_csv("logins-2016-2020.csv")

# Transform wide to long
var_names = ["Logins 2016", "Logins 2017", "Logins 2018", "Logins 2019", "Logins 2020"]
df = pd.melt(df, id_vars = ["Date"], value_vars = var_names)
df = df.dropna()

# Drop "Logins " and keep just the year
df['year'] = df['variable'].str.replace(r'\D', '')

# Plot the annual logins
annual_logins = df.groupby(["year"]).sum()
plt.plot(annual_logins["value"])
plt.show()

# Convert year to integer
# df["year"] = pd.to_numeric(df['year'])

# Separate date column into month and day

# Combine into one date column

# Uncount the n column
