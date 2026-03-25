Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arithematic
a=1
b=2
print(a+b)
3
print(a-b)
-1
print(a*b)
2
print(a/b)
0.5
print(a//b)
0
print(a**b)
1
print(a%b)
1
#assignment
a=1
b=2
print(a+=b)
SyntaxError: invalid syntax
>>> a+=b
>>> a
3
>>> a-=b
>>> a
1
>>> a*=b
>>> a
2
>>> a/=b
>>> b
2
>>> a//=b
>>> b
2
>>> a%=b
>>> b
2
>>> a**=b
>>> b
2
>>> #comparision
>>> a=1
>>> b=2
>>> print(a<=b)
True
>>> print(a>=b)
False
>>> print(a!=b)
True
>>> print(a==b)
False
>>> print(a>b)
False
>>> print(a<b)
True
>>> #logical
>>> print(a>b)&(a<b)
False
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(a>b)&(a<b)
TypeError: unsupported operand type(s) for &: 'NoneType' and 'bool'
a=1
b=2
(a>b)and(a<b)
False
(a<b)and(a>b)
False
(a<b)and(b>a)
True
(a>b)or(a<b)
True
(a<b)or(a>b)
True
(a>b)or(b<a)
False
(a<b)not(b>a)
SyntaxError: invalid syntax
a<b not b>a
SyntaxError: invalid syntax
not true
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
not True
False
not False
True
True
True
(a!<b)and(b==a)
SyntaxError: invalid syntax
(a!=b)and(b==a)
False
(a<=b)and(b==a)
False
#(a!=b)and(b==a)


#identify
a=3
if type(a) is int:
    print("true")

    
true
if type(a) is float:
    print("true")

    
a=3.2
if type(a) is float:
    print("true")

    
true
if type(a) is not int:
    print("true")

    
true
#membership
a=1,2,3,4,5,6,7,8,9
if 3 in a:
    print("10")

    
10
if 10 in a:
    print("20")

    
#Bitwise
    
a=1
b=2
a&b
0
bin(1)
'0b1'
bin(2)
'0b10'
a|b
3
a^b
3
#not
a=1
~a
-2
#leftshift
a=3
a<<2
12
#rightshift
a=3
a>>2
0
