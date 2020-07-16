import numpy as np 
import pandas as pd 
from pandas import Series, DataFrame

name = []
dob = []
occu = []
height = []
new_list = []
new_dict = []

for i in range(3):
  name.append(input('Please enter your name:'))
  dob.append(input('Please enter your date of birth:'))
  occu.append(input('Please enter your occupation:'))
  height.append(input('Please enter your height:'))

mid = map (list,zip(name, dob, occu, height))
for item in mid:
  new_dict=dict(zip(['name','dob','occu','height'],item))
  new_list.append(new_dict)

data = pd.Series(new_list)
datafr = DataFrame(new_list, index = name)
print(datafr)

#################################################################################

import numpy as np
import pandas as pd
data = {
    "birth": [],
    "job": [],
    "height": [],
  }
names = []
for i in range(4):
  name = input("What is your name? ")
  birth = input("When is your birthday? ")
  job = input("What is your occupation? ")
  height = input("What is your height? ")
  data["birth"].append(birth)
  data["job"].append(job)
  data["height"].append(height)
  names.append(name)
series = pd.Series(data)
frame = pd.DataFrame(data, index = names)

print(frame)