import pandas as pd

s1 = pd.Series([1,2,3,4,5,12,11,123])
s2 = pd.Series(["a","b","c","d","e","f","g","h"])

df = pd.DataFrame(columns=["numbers","letters"])
df["numbers"] = s1
df["letters"] = s2

# indexing
df["letters"]
#Add
df.insert(2, "more letters", ['g','c','d','e','f','g','h','i'])
# Delete
df = df.drop("letters", axis = 1)