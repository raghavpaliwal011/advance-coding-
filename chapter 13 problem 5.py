from functools import reduce
l = [4,8,4,255,545]

a = reduce(max,l)
print(a)
