#!/usr/bin/python3
# reading a csv file and adding new rows to it
import pandas as pd

df = pd.read_csv("class.csv")
print(type(df))
print(df)

print("adding new rows")	# the list is to avoid scalar values
new_row = {"Name": ["Morty", "Summer"], "Age": [14, 16], "Average": [4, 7], "Discount": [False, True], "Percentage": [0, 15]}

df2 = pd.DataFrame(new_row)
print(df2)

df = pd.concat([df, df2], ignore_index=True)
df.reset_index()
print(df)
