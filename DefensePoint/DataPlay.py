import csv
import pandas as pd
import matplotlib.pyplot as mp

# read csv and take set rows
data = pd.read_csv("data.csv", nrows=25)

# select 2 columns
df = pd.DataFrame(data, columns=["discounted_price", "rating"])

# remove the currency symbol in the discounted_price column
df['discounted_price'] = df['discounted_price'].str.replace('₹', '')

# remove the comma in the discounted_price column
df['discounted_price'] = df['discounted_price'].str.replace(',', '')

# replace nan values with zero
df['discounted_price'] = df['discounted_price'].fillna(0)

# replace nan values with zero
df['rating'] = df['rating'].fillna(0)

# cast the value in the discounted_price column to float
df['discounted_price']=df['discounted_price'].astype(float)

# cast the rating value into float
df['rating']=df['rating'].astype(float)

# plot the dataframe
df.plot(x="discounted_price", y=["rating"], kind="bar", figsize=(16, 9))

# print bar graph
mp.show()