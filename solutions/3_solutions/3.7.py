import pandas as pd

s1 = pd.Series([1,2,3,4,5,12,11,123])
s2 = pd.Series(["a","b","c","d","e","f","g","h"])

df = pd.DataFrame(columns=["numbers","letters"])
df["numbers"] = s1
df["letters"] = s2

# df = pd.DataFrame({"numbers":s1, "letters":s2})
df.size
# add a column
df.insert(2, "more letters", ['g','c','d','e','f','g','h','i'])
# Boolean indexing
df[df["numbers"] > 10]