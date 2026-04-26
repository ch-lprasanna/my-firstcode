#*arguments->*is used to unpack the elements
'''a=[2,3,4,5,6,7,8]
print(a)
print(*a)#without comma
print(type(a))'''

a=(2,3,4,5,6,7,8)
print(a)
print(*a)
print(type(a))

'''a={2,3,4,5,6,7,8}
print(a)
print(*a)
print(type(a))'''

'''a={"year":2026,"month":4}
print(a)
print(*a)
print(type(a))'''#only keywords

'''a="codegnan"
print(a)
print(*a)
print(type(a))'''

'''a,b,c=1,2,3
print(a)
print(b)
print(c)'''

'''a,b,c=1,2,3,4,5,6,7
print(a)
print(b)
print(c)'''#more than 3 values

'''a,*b,c=1,2,3,4,5,6,7
print(a)
print(*b) #here * is given in any var to store values
print(c)'''

'''a,b,c="pyt"
print(a)
print(b)
print(c)'''

'''a,b,c="python"
print(a)
print(b)
print(c)'''#error

'''a,b,*c="python"
print(a)
print(b)
print(*c)'''


#variable length arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7)
b=[3,4,5,6,7,8]
check(*b)
c=(4,5,6,7,8)
check(*c)
d={8,9,10,11,12}
check(*d)
e={"name":"prasanna","year":2026}
check(*e)'''

'''def check1(*a):
    d=2#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6,7)
check1(2,3,4.3,5,5.2)
check1(2,4,6,4.3,5.2,"prasanna")'''

#kwags(**)
'''def check(**a):
    print(a)
    print(type(a))
check()
d={"idnos":[10,20,30],
   "names":["lakshmi","megana","devi"],
   "status":["p","a","p"]}
check(**d)'''

'''def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check()
d={"idnos":[10,20,30],
   "names":["lakshmi","megana","devi"],
   "status":["p","a","p"]}
check(**d)'''

#both * and ** usage
'''def final(*a,**b):
    d=3
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5,6.4,3.5)
final(*data)
details={"names":["prasanna","navya"],
         "places":["vij","hyd"]}
final(**details)
final(*data,**details)'''
