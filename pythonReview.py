########################################################################################################################################
#\n means enter \t means table format
print('hello \nworld')

########################################################################################################################################
# String Immutability
name = "Sam"
# name[0] = 'P' string cannot be changed; Any change to the string, you have to create a new one
Last_name = name[1:3]
print('P' + Last_name)

########################################################################################################################################
#Plus of String 
x = 'string'
x = x + "Plus"
print(x)

########################################################################################################################################
# Multiplication of string 
letter = 'z'
print(letter * 5)

########################################################################################################################################
# number can add; string number cannot add
print(2 + 3)
print('2' + '3')

########################################################################################################################################
# common string functions
x = 'All capitalize'
print(x.upper()) # all upper characters
x.lower() # all lower characters
x.split() # split the string

########################################################################################################################################
y = 'This string is split by character i'
y = y.split('i')
print(y)

########################################################################################################################################
# string format()  
print('This is a string {}'.format('Inserted'))
print('The {} {} {}'.format('apple', 'boys', 'check'))
print('The {2} {1} {0}'.format('apple', 'boys', 'check')) # format() Use index to determine the format print
print('The {0} {0} {0}'.format('apple', 'boys', 'check'))
# print('The {} {} {}'.format(a = 'apple', b = 'boys', c = 'check'))
print('The {c} {b} {a}'.format(a = 'apple', b = 'boys', c = 'check'))
print('The {c} {c} {c}'.format(a = 'apple', b = 'boys', c = 'check'))

########################################################################################################################################
# float number format()
floatNumber = 100/777
print(floatNumber) 
print('The result is {fNum: 1.3f}'.format(fNum = floatNumber)) # 1.3f stands for one digit before decimal; three digits behind decimal
print('The result is {fNum: 10.5f}'.format(fNum = floatNumber))

########################################################################################################################################
# Python 3.6 new formatting
newFormat = 'Charles'
print('The name is {}'.format(newFormat))
print(f'The name is {newFormat}')

name = 'Charles'
age = '23'
print(f'{name} is {age} years old')

########################################################################################################################################
# Python list
# List can be changed; String cannot be changed
my_List = ['string', 100, 23.2] #python list can have multiple type
print(len(my_List)) # len() return length of the list

myList = ['One', 'Two', 'Three']
print(myList[1])
print(myList[1:3])

anotherList = ['Four', 'Five', 'Six']
resultList = myList + anotherList
print(resultList) # won't change original list
print(myList)
print(anotherList)

resultList[0] = 'CHANGED'
print(resultList)

resultList.append('Seven') # Add element at the end of list
print(resultList)

popped = resultList.pop()
print(popped)

resultList.pop(0) # Use index to indicate the element to be removed
resultList.pop(-1) # remove the last one reverse index works! 
print(resultList)

sortList = ['a', 'g', 'h', 'b', 'z']
numList = [1, 52134234, 2, 9788]
sortList.sort()
numList.sort()
print(sortList, numList)

numList.reverse() # reverse the list
print(numList)

# Nested list
nestedList = [1, 2, [3,4]]
# To get 4 in list
print(nestedList[2][1])

########################################################################################################################################
# Python dictionaries
my_dict = {'key1' : 'value1', 'key2' : 'value2'}
print(my_dict)
print(my_dict['key1'])

price_lookup = {'apple' : 2.99, 'oranges' : 3.99, 'milk' : 6.99} 
print(price_lookup['apple'])

# dictionary is flexibile in types
d = {'k1' : 1, 'k2' : [0, 1, 2], 'k3' : {'key' : 'anotherDict'}}
print(d['k2'][2])
print(d['k3']['key'])

# Add or replace dict
myDict = {'key1' : 100, 'key2' : 200}
myDict['key3'] = 300
print(myDict)

myDict['key1'] = 'NEW VALUE'
print(myDict)

print(myDict.keys())
print(myDict.values())
print(myDict.items())

########################################################################################################################################
# Python Tuples
t = ('one', 2, 3.0)
l = [1, 2, 3]
print(type(t), len(t), t[0], t[-1]) 

t = ('a', 'a', 'b')
print(t.count('a'), t.index('a')) # count() times of a; index() first time showup of a

########################################################################################################################################
# Python set: no replicated element in set
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)

myList = [5,5,5,5,2,22,8,5,11,1,1,1,1,1] # remove duplicated elements when call set()
print(set(myList))

########################################################################################################################################
# Python boolean
b = None
print(1 == 1, 1 > 2, type(True), b)

########################################################################################################################################
# file I/O
myfile = open('pythonReview.txt')
print(myfile.read())

myfile.seek(0) # To reset read otherwise when call read() again, nothing can be read

print(myfile.readlines())
myfile.close() # Error if no close()

with open('pythonReview.txt', mode = 'r') as my_new_file:
	contents = my_new_file.read()
	print(contents)
# r : reading
# w : writing/ over writing/ creating a new file if not exist
# a : adding
# r+ : reading and writing
# w+ : over writing and reading 

with open('pythonReview.txt', mode = 'r') as f:
	print(f.read())

with open('pythonReview.txt', mode = 'a') as f:
	f.write('\nFOUR ON FOURTH')

with open('newPythonReview.txt', mode = 'w') as f:
	f.write('I CREATED THIS NEW FILE') 

########################################################################################################################################
# Python comparision
print(1 == 1, 1 == 2, 'hello' == 'bye', 2.0 == 2, 3 >= 3, 3 != 3)

print(1 < 2 and 2 < 3)
print((1 < 2) and (2 < 3))
print(100 == 1 or 1 == 1)
print(not 1 == 1)

########################################################################################################################################
# if Elif Else
happy = True

if happy:
	print('Smile')
else:
	print('Cry')

loc = 'Bank'

if loc == 'Auto Shop':
	print("Cars")
elif loc == 'Bank':
	print("Money")
elif loc == 'Store':
	print("Goods")
else:
	print("IDK")




















