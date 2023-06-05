l1 = [3, 55, 41, 23, 89, 44, 12] # you can also add a diff data type in this
l1[0]=12
print(type(l1))
print(l1)
# l1.remove(44)
# l1.remove(44, 12 ) # will give error
# print(l1)
# Strings are immutable which means they annot be changed while lists are not,, also this means
# whenever we are using string methods we also create new strings

l1.sort()
print(l1)

l1.append(56)
print(l1)
#
# l1.clear()
# print(l1)

l1.extend([89,123,475,2365,412])
print(l1)

l1.index(56)
print(l1)

# slicing
print(l1[2:5])


