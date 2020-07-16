import pandas as pd
pd.set_option('display.expand_frame_repr', False)

url = "https://pynative.com/wp-content/uploads/2019/01/Automobile_data.csv"
#read
df = pd.read_csv(url)
df.head()
#Add
new_col = df["price"]/df["horsepower"]
df.insert(0,"horse price", new_col, True)
#Delete
df = df.dropna()
df = df.reset_index(drop  = True)