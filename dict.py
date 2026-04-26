Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dict
>>> a={"name":"pooja","year":2026,"month":3}
>>> print(a)
{'name': 'pooja', 'year': 2026, 'month': 3}
>>> type(a)
<class 'dict'>
>>> b={"name","year","month"}
>>> type(b)
<class 'set'>
>>> a.keys()
dict_keys(['name', 'year', 'month'])
>>> a.values()
dict_values(['pooja', 2026, 3])
>>> a.items()
dict_items([('name', 'pooja'), ('year', 2026), ('month', 3)])
>>> a={"name":"pooja","year":2026,"month":3}
>>> a.update({"year":2026})
>>> a
{'name': 'pooja', 'year': 2026, 'month': 3}
>>> a.update({"month":3},{"time":10})
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.update({"month":3},{"time":10})
TypeError: update expected at most 1 argument, got 2
>>> a.update({"month":3,"time":10})
>>> a
{'name': 'pooja', 'year': 2026, 'month': 3, 'time': 10}
>>> a={"mailid","prasanna@code.com"}
>>> a.setdefault("name","prasanna")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.setdefault("name","prasanna")
AttributeError: 'set' object has no attribute 'setdefault'
>>> a={"mailid":"prasanna@code.com"}
>>> a.setdefault("name","prasanna")
'prasanna'
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("name")
'prasanna'
a.pop("prasanna@code.com")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.pop("prasanna@code.com")
KeyError: 'prasanna@code.com'
a.copy()
{'mailid': 'prasanna@code.com'}
a.clear()
a
{}
b={}
b.update({"day":"tuesday"})
b
{'day': 'tuesday'}
a
{}
a={"city":"vja","country","india"}
SyntaxError: ':' expected after dictionary key
a={"city":"vja","country":"india"}
a.get("country")
'india'
a
{'city': 'vja', 'country': 'india'}
a["city"]
'vja'
a
{'city': 'vja', 'country': 'india'}
a.popitem()
('country', 'india')
a
{'city': 'vja'}
a={"idnos":[10,20,30],"names":["mano","kirt","lav"]}
print(a)
{'idnos': [10, 20, 30], 'names': ['mano', 'kirt', 'lav']}
type(a)
<class 'dict'>
a.keys()
dict_keys(['idnos', 'names'])
a.values()
dict_values([[10, 20, 30], ['mano', 'kirt', 'lav']])
a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['mano', 'kirt', 'lav'])])
#duplicate
a={"name":"prasa","city":"vij","name","prasa"}
SyntaxError: ':' expected after dictionary key
a={"name":"prasa","city":"vij","name":"prasa"}
print(a)
{'name': 'prasa', 'city': 'vij'}
a={"name":"prasa","city":"vij","name1":"prasa"}
print(a)
{'name': 'prasa', 'city': 'vij', 'name1': 'prasa'}
