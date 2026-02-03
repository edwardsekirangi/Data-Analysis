import pandas as pd

df = pd.read_csv('pokemon_data.csv')

#df = pd.read_csv("pokemon_data.txt")
#print(df)

#READING DATA IN PANDAS

#read headers
print(df.columns)

#read each column
#print(df[["Name", "Type 1", "HP"]] [0:5])

#Read each fow
#print(df.iloc[1:4])

#print(df.iloc[2,1])

#iterate through rows
#for index, row in df.iterrows():
#    print(index, row["Name"])
#print (df.loc[df["Type 1"] == "Fire"])

#Mean standard deviation type stats
#print(df.describe())

#SORTING /DESCRIBING DATA
#print(df.sort_values("Name", ascending=False))

#Making Changes to data
#print(df.head(5))

#Creating a total column for our stats