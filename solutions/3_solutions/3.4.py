import numpy as np 
import pandas as pd 

name = input('Please enter your name:') 
dob = input('Please enter your date of birth:')
occu = input('Please enter your occupation:')
height = input('Please enter your height:')
myDict = {
	name: [dob, occu , height]
}
data = pd.Series(myDict)
print(data)