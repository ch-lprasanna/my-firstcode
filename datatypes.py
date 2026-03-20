Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=4
>>> type(a)
<class 'int'>
>>> b=3.4
>>> type(b)
<class 'float'>
>>> c="string"
>>> type(c)
<class 'str'>
>>> d=4+6j
>>> type(d)
<class 'complex'>
>>> e=True
>>> print(e)
True
>>> type(e)
<class 'bool'>
>>> e=true
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    e=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> f=true
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    f=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> f=False
>>> f=false
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    f=false
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> f="false"
>>> type(f)
<class 'str'>
>>> e="true"
>>> type(e)
<class 'str'>
>>> d=5j
type(d)
<class 'complex'>
d=5
type(d)
<class 'int'>
