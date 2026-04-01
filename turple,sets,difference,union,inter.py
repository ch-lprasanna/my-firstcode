Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple()
>>> a=(1,2.3,"python",3+6j,True,False)
>>> type(a)
<class 'tuple'>
>>> len(a)
6
>>> a.count(True)
2
>>> a.index("2.3")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.index("2.3")
ValueError: tuple.index(x): x not in tuple
>>> a.index(2.3)
1
>>> #sets{}
>>> a={2,3.4,"java",6+9j.True,False}
SyntaxError: invalid syntax
>>> a={2,3.4,"java",6+9j,True,False}
>>> type(a)
<class 'set'>
>>> print(a)
{False, True, 2, 3.4, (6+9j), 'java'}
>>> a={4,3,6,7,0}
>>> a.add(50)
>>> a
{0, 50, 3, 4, 6, 7}
>>> #issubset()
>>> a={1,2,3,4,5}
>>> b={8,9,7,6,5}
>>> a.issubset(b)
False
>>> a={1,2,3,4,5,6,7}
>>> b={4,5,6,7}
>>> b.issubset(a)
True
>>> 
>>> a.issubset(b)
False
>>> a.issuperset(b)
True
#union
a={4,5,6,7,8,9}
b={5,6,7,8,9,10,0}
a.union(b)
{0, 4, 5, 6, 7, 8, 9, 10}
#intersection()
a={2,3,4,5,6,7,8,9,10}
b=(11,12,13,14,8,9,10}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
b={11,12,13,14,8,9,10}
a.intersection(b)
{8, 9, 10}
#diff
a={1,2,3,4,5,6,7,}
b={1,2,3,4,5}
c={6,7,8,1,23}
b.difference(c)
{2, 3, 4, 5}
c.difference(b)
{8, 7, 6, 23}
3update
SyntaxError: invalid decimal literal
#update
a={1,2,3,4,5,6,7,}
b={1,2,3,4,5}
SyntaxError: multiple statements found while compiling a single statement
a={1,2,3,4,5,6,7,}b={1,2,3,4,5}
SyntaxError: invalid syntax
a={1,2,3,4,5,6,7}
b={1,2,3,4,5}
a.update(b)
b
{1, 2, 3, 4, 5}
b.update(a)
a
{1, 2, 3, 4, 5, 6, 7}

a
{1, 2, 3, 4, 5, 6, 7}
b
{1, 2, 3, 4, 5, 6, 7}
#symdiff
a={1,2,3,4,5,6,7,8}
b={1,2,3,10,12,13,4,5}
a.symmetric_difference(b)
{6, 7, 8, 10, 12, 13}
a.symmetric_difference(b)
{6, 7, 8, 10, 12, 13}
b.symmetric_difference(a)
{6, 7, 8, 10, 12, 13}
a={2,4,6,8,10,12,14}
b={1,2,3,5,7,8,10,12}
a.symmetric_difference(b)
{1, 3, 4, 5, 6, 7, 14}
a
{2, 4, 6, 8, 10, 12, 14}
a.differenceupdate(b)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a.differenceupdate(b)
AttributeError: 'set' object has no attribute 'differenceupdate'. Did you mean: 'difference_update'?
a.difference_update(b)
a
{4, 6, 14}
a
{4, 6, 14}
b.differenceupdate(a)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    b.differenceupdate(a)
AttributeError: 'set' object has no attribute 'differenceupdate'. Did you mean: 'difference_update'?
b.difference_update(a)
b
{1, 2, 3, 5, 7, 8, 10, 12}
