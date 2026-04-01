Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #list
>>> a=[4,6.7,"prasanna",5+9j,True,False]
>>> print(a)
[4, 6.7, 'prasanna', (5+9j), True, False]
>>> type(a)
<class 'list'>
>>> b=60
>>> print(b)
60
>>> b=[6]
>>> type(b)
<class 'list'>
>>> #append
>>> a=["python","c","java","c++"]
>>> a.
SyntaxError: invalid syntax
>>> a.append["html"]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.append["html"]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a.append("html")
>>> a
['python', 'c', 'java', 'c++', 'html']
>>> a.append("sql","ui")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.append("sql","ui")
TypeError: list.append() takes exactly one argument (2 given)
>>> a.append(["sql","ui"])
>>> a
['python', 'c', 'java', 'c++', 'html', ['sql', 'ui']]
>>> #extend
>>> a=["apple,"mango","orange"]
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> a=["apple","mango","orange"]
...    
>>> a=["apple","mango","orange"]
...    
a.extend(["mango","kiwi"])
   
#extend()
   
a=["apple","mango","orange"]
   
a=["python","c","java","c++"]
   
a=["c","c++","java"]
   

a=["c","c++","java"]
   
a=["c","c++","java"]
   
