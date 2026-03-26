Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="vijayawada"
a[1]
'i'
a[3]
'a'
a="i am in class"
a[2]
'a'
a[-1]
's'
a[1]
' '
a[2]+a[3]
'am'
a[1]+a[4]
'  '
a=
SyntaxError: invalid syntax
a="time is very precious"
a[8]+a[9]+a[10}a[11]
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a[8]+a[9]+a[10]+a[11]
'very'
a[13]+a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
'precious'
a[0]+a[1]+a[2]+a[3]
'time'
a="vijayawada is a royal city"
a[16]+a[17]+a[18]+a[19]+a[20]
'royal'
a[22]+a[23]+a[24]+a[25]
'city'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]
'vijayawada'
a="I am learning python course"
a[14]+a[15]+a[16]+a[17]+1[18]+a[19]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a[14]+a[15]+a[16]+a[17]+1[18]+a[19]
TypeError: 'int' object is not subscriptable
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
a[21]+a[22]+a[23]+a[24]+a[25]+a[26]
'course'
a[5]+a[6]+a[7]+a[8]+a[9]+a[10]+a[11]+a[12]
'learning'
a[2]+a[3]
'am'
#negative
a="I love python"
a[-8]+a[-9]+a[-10]+[-11]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a[-8]+a[-9]+a[-10]+[-11]
TypeError: can only concatenate str (not "list") to str
a[-8]+a[-9]+a[-10]+a[-11]
'evol'
a[-11]+a[-10]+a[-9]+a[-8]
'love'
a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'python'
b="vizg is a city of Destiny"
b[-7]+b[-6]
'De'
b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'Destiny'
a[-15]+a[-14]+a[-13]+a[-12]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a[-15]+a[-14]+a[-13]+a[-12]
IndexError: string index out of range
b[-15]+b[-14]+b[-13]+b[-12]
'city'
b[-25]+b[-24]+b[-23]+b[-22]+b[-21]
'vizg '
#slicing
a="codegnan"
a[0:4]
'code'
a[:4]
'code'
a[4:8}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a[4:8]
'gnan'
a[4:]
'gnan'
a[1:4]
'ode'
a="work until you succeed"
a[0:4]
'work'
a[11:14]
'you'
a[5:10]
'until'
a[12:14]
'ou'
>>> a[11:14]
'you'
>>> a="simple is better than complex"
>>> a[17:21]
'than'
>>> a[13:16]
'ter'
>>> a[10:16]
'better'
>>> a[0:6]
'simple'
>>> a[22:29]
'complex'
>>> #negitive
>>> a="codegnan if solutions"
>>> a[-1:-10]
''
>>> a[-1:-9]
''
>>> a[-9:-1]
'solution'
>>> a[-9:-10]
''
>>> a[-9:-11]
''
>>> a[-12:-10]
'if'
>>> a[-21:-11]
'codegnan i'
>>> a[-21:-12]
'codegnan '
>>> b="beautiful is better than ugly"
>>> b[-4:-0]
''
>>> b[-4:]
'ugly'
>>> b[-16:-10]
'better'
>>> b[-29:-20]
'beautiful'
