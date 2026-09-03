keys = ['a','b','c','d','e']
values = [1, 2, 3, 4, 5, 2,3]

d = {k:v for (k,v) in zip(values, keys)}
print (d)