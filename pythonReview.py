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



























