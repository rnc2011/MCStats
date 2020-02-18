library(tidyverse)
library(lubridate)

# Read in the data
df <- read_csv("logins-2016-2020.csv")

# Transform wide to long
# Drop "Logins " and keep just the year
df <- df %>%
  pivot_longer(
    starts_with("Logins "),
    names_to = "year",
    names_prefix = "Logins ",
    values_to = "n",
    values_drop_na = TRUE
  )

# Plot the annual logins
annual_logins <- df %>%
  group_by(year) %>%
  summarise(n = sum(n))
annual_logins %>%
  ggplot(aes(x = year, y = n, group = 1)) +
  geom_line()

# Convert year to integer
df <- df %>%
  mutate(year = as.integer(year))

# Separate date column into month and day
df <- df %>%
  separate(Date, into = c("month", "day"), sep = "-", convert = TRUE)

# Combine into one date column
df <- df %>%
  unite(date, year, month, day, sep = "-") %>%
  mutate(date = ymd(date))

# Uncount the n column
df <- df %>%
  uncount(n)
