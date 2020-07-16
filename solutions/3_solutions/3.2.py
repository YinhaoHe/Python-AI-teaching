import numpy as np
import pandas as pd

index = [chr(i) for i in range(97,123)]
data = pd.Series([i for i in range(1, 27)], index = index)
print(data)

# import numpy as np
# import pandas as pd


# a = np.arange(1, 27)
# d = {}
# for n in a:
# 	d[chr(n + 96)] = n
# 	d[chr(n + 64)] = n

# print(d)
# p = pd.Series(d)
# print(p)
