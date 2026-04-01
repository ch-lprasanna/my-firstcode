Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=["black","white","red"]
>>> \
...   a.sort()
SyntaxError: unexpected indent
>>> a.sort()
>>> a
['black', 'red', 'white']
>>> b=["hyd","bng","vja"]
>>> b.sort()
>>> b
['bng', 'hyd', 'vja']
>>> a=["c","ds","ml"]
>>> a.reverse()
>>> a
['ml', 'ds', 'c']
>>> a=["python","c","java","c++"]
>>> a.sort()
>>> a
['c', 'c++', 'java', 'python']
>>> ['c', 'c++', 'java', 'python']
['c', 'c++', 'java', 'python']
>>> #pop
>>> a.pop["html","css","js"]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.pop["html","css","js"]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a=["html","css","js"]
>>> a.pop()
'js'
>>> a.pop("js")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.pop("js")
TypeError: 'str' object cannot be interpreted as an integer
>>> a.pop(2)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.pop(2)
IndexError: pop index out of range
KeyboardInterrupt
a.pop(1)
'css'
a.remove(a)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.remove(a)
ValueError: list.remove(x): x not in list
a=["python","c","java","c++"]
a.clear()
a
[]
b=[]
b.append("prasanna")
b
['prasanna']
a=["python","c","java","c++"]
a.copy()
['python', 'c', 'java', 'c++']
b=a.copy()
b
['python', 'c', 'java', 'c++']
c="hello"
len(c)
5
c=["hello"]
len(c)
1
a.remove("python")
a
['c', 'java', 'c++']
a.count("c")
1
#pop
a.pop["html","css","js"]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.pop["html","css","js"]
TypeError: 'builtin_function_or_method' object is not subscriptable
#pop
a=["html","css","js"]
a.pop(2)
'js'
a.pop()
'css'
a
['html']
#remove
a=["html","css","js"]
a.remove(a)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.remove(a)
ValueError: list.remove(x): x not in list
a.remove(0)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.remove(0)
ValueError: list.remove(x): x not in list
a.remove("html")
a
['css', 'js']
a=["black","white","red"]
a.sort()
a
['black', 'red', 'white']
a=["c","ds","ml"]
a.sort()
a
['c', 'ds', 'ml']
a.insert=(["1","java"])
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.insert=(["1","java"])
AttributeError: 'list' object attribute 'insert' is read-only
a.insert(["1","java"])
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.insert(["1","java"])
TypeError: insert expected 2 arguments, got 1
a.insert("java")
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.insert("java")
TypeError: insert expected 2 arguments, got 1
a.index("graphes")
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.index("graphes")
ValueError: list.index(x): x not in list
a=["apple","org","kiwi"]
a.index("graphes")
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.index("graphes")
ValueError: list.index(x): x not in list
a.index("org")
1
a.insert(["1","bananna"])
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a.insert(["1","bananna"])
TypeError: insert expected 2 arguments, got 1
a.insert([1,"bananna"])
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a.insert([1,"bananna"])
TypeError: insert expected 2 arguments, got 1
a.insert(['1','bananna'])
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.insert(['1','bananna'])
TypeError: insert expected 2 arguments, got 1
