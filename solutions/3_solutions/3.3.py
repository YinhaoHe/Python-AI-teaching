import numpy as np
import pandas as pd

randOrder = np.random.randint(97,124,26)
index_arr = randOrder - 96
print(index_arr)
print(pd.Series([chr(i) for i in randOrder], index = index_arr))