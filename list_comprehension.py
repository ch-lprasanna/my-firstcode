#list comprehension
#a=[epress for var in range/collection]
a=["add","sub","mul"]
'''print(a.upper())'''#error
'''b=str(a)
print(b.upper())'''
'''for i in a:
    print(i.upper())'''

'''for i in a:
    print(i.upper(),end=" ")'''

'''b=[i.upper() for i in a]
print(b)'''

'''a=[2,3,4,5,6]
b=[i**2 for i in a]#or
b=[i*i for i in a]#or
b=[pow(i,2) for i in a]
print(b)'''

#if usage (0 to 16 even nums)
'''a=[i for i in range(16) if i%2==0]
print(a)'''

'''a=[i*i if i%2==0 else i*5 for i in range(21)]
print(a)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
#print(a+b)
c=[a[i]+b[i] for i in range(len(a))]
print(c)
