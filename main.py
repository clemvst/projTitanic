import pandas as pd

df = pd.read_csv("train.csv")
df = df[["Survived", "Sex", "Age"]]
print(df)
