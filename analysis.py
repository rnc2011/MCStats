import pandas as pd

# Read in the data
df = pd.read_csv("logins-2016-2020.csv")

# Transform wide to long
var_names = ["Logins 2016", "Logins 2017", "Logins 2018", "Logins 2019", "Logins 2020"]
df = pd.melt(df, id_vars = ["Date"], value_vars = var_names)
df = df.dropna()

# Get just the year
df['variable'] = df['variable'].str.replace(r'\D', '')
# Convert year to integer

# Plot the annual logins


# Separate date column into month and day

# Combine into one date column

# Uncount the n column
