import numpy as np
import pandas as pd

index = [chr(i) for i in range(97,123)]
data = pd.Series([i for i in range(1, 27)], index = index)
print(data)