import csv
import pandas as pd

data = []

with open('merged.csv') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)
headers = data[0]
headers.pop(-1)
rows = data[1:]

for i in rows:
    i.pop(-1)

df = pd.DataFrame(rows,columns=headers)
df.dropna(subset = headers, inplace=True)

df.to_csv('final.csv')