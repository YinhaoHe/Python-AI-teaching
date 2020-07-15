# Original sort and sorted
# sort() change the original list, no return
# sorted() new a list, and return that list, no affect original list

a = [2, 1, 4, 9, 6]
a.sort()
print a
 
c = [2, 1, 4, 9, 6]
d = sorted(c)
print d
print c

# Output
# [1, 2, 4, 6, 9]
# [1, 2, 4, 6, 9]
# [2, 1, 4, 9, 6]

####################################################################################

# Based on cmp

L = [('a', 3), ('d', 2), ('c', 1), ('b', 4)]
a = sorted(L, cmp=lambda x, y : cmp(x[0], y[0]))
b = sorted(L, cmp=lambda x, y : cmp(x[1], y[1]))
print L
print a
print b

# Output
# [('a', 3), ('d', 2), ('c', 1), ('b', 4)]
# [('a', 3), ('b', 4), ('c', 1), ('d', 2)]
# [('c', 1), ('d', 2), ('a', 3), ('b', 4)]

####################################################################################

# Based on Key

L = [('a', 3), ('d', 2), ('c', 1), ('b', 4)]
a = sorted(L, key=lambda x : x[0])
b = sorted(L, key=lambda x : x[1])
print L
print a
print b

# Output

# [('a', 3), ('d', 2), ('c', 1), ('b', 4)]
# [('a', 3), ('b', 4), ('c', 1), ('d', 2)]
# [('c', 1), ('d', 2), ('a', 3), ('b', 4)]

####################################################################################

# Based on reverse

L = [2, 1, 4, 9, 6]
a = sorted(L, reverse=True)
b = sorted(L, reverse=False)
print L
print a
print b

# Output

# [2, 1, 4, 9, 6]
# [9, 6, 4, 2, 1]
# [1, 2, 4, 6, 9]

####################################################################################