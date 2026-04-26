#generators
'''a=[i for i in range(16)]
print(a)
print(type(a))'''

'''a=(i for i in range(16))
print(*a)
print(type(a))'''

a=(i for i in range(16))
#print(*a)
#print(list(a))
#print(tuple(a))
print(set(a))
