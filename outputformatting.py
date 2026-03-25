Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #string methods
>>> #len
>>> a="codegnan"
>>> len(a)
8
>>> a=" "
>>> len(a)
1
>>> a=""
>>> len(a)
0
>>> a="python course"
>>> len(a)
13
>>> #count
>>> a="twinkle twinkle little star"
>>> a.count("twinkle")
2
>>> a.count(" ")
3
>>> a.count("i")
3
>>> #find a string
>>> a="code"
>>> a.fing("d")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.fing("d")
AttributeError: 'str' object has no attribute 'fing'. Did you mean: 'find'?
>>> a.find("d")
2
>>> a="code gnan"
>>> a.find("g")
5
>>> a="the python fullstack"
>>> a.find("python")
4
>>> a.find("fullstack")
11
>>> #escape sequences
\n
SyntaxError: unexpected character after line continuation character
#\n
#\tab
a="name:prasanna\nmailid:chengalasettylakshmiprasanna3@gmail.com\tcity:vijayawada"
print("a")
a
print(a)
name:prasanna
mailid:chengalasettylakshmiprasanna3@gmail.com	city:vijayawada
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
a="wait wait until you succeed"
a.replace("wait","work"1)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a.replace("wait","work",1)
'work wait until you succeed'
a.replace("wait","work",0)
'wait wait until you succeed'
a.replace("wait","work",2)
'work work until you succeed'
#upper
a="hello"
a.upper()
'HELLO'
#lower
a="HELLO"
a.lower()
'hello'
#capitalize
a="python'
SyntaxError: unterminated string literal (detected at line 1)
a="python"
a.capitalize()
'Python'
#title
a="my course python"
a.title()
'My Course Python'
a.capitalize
<built-in method capitalize of str object at 0x0000021773A577F0>
a.capitalize()
'My course python'
#true or false
a="python"
a.isalpha()
True
a.isupper()
False
a.islower()
True
a.startswith("p")
True
a.endswith("n")
True
a.isdigits()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.isdigits()
AttributeError: 'str' object has no attribute 'isdigits'. Did you mean: 'isdigit'?
a="123"
a.isdigits()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.isdigits()
AttributeError: 'str' object has no attribute 'isdigits'. Did you mean: 'isdigit'?
a.isdigit()
True
a="hi123"
a.isalnum()
True
a="hi"
a.isalnum()
True
a="1"
a.isalnum()
True
#strip
#lstrip,#rstrip
a="      prasanna    "
a.strip()
'prasanna'
a.lstrip()
'prasanna    '
a.rstrip()
'      prasanna'
#split
a="python fullstack course"
a.split()
['python', 'fullstack', 'course']
#join
a="htmlcssjs"
""a.join()
SyntaxError: invalid syntax
"".join(a)
'htmlcssjs'
"is".join(a)
'histismisliscississisjiss'
" is ".join(a)
'h is t is m is l is c is s is s is j is s'
a="html","css","js"
"is".join(a)
'htmliscssisjs'
" is ".join(a)
'html is css is js'
#concatenation
a="prasanna"
b="ch"
print(a+b)
prasannach
print(a+""+b)
prasannach
print(a+" "+b)
prasanna ch
print((a+" "+b).title())
Prasanna Ch
print((a+" "+b).capitalize())
Prasanna ch
print(a.title()+" "+b.title())
Prasanna Ch
#formatting
a=1
b=2
print(a+b)
3
print("the sum is",a+b)
the sum is 3
a=oyee
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    a=oyee
NameError: name 'oyee' is not defined
a=oye
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    a=oye
NameError: name 'oye' is not defined
a="oye"
b="prasanna"
print("hello {} {}".formatting(a,b))
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    print("hello {} {}".formatting(a,b))
AttributeError: 'str' object has no attribute 'formatting'
print("hello {} {}".format(a,b))
hello oye prasanna
print("hello [] []".format(a,b))
hello [] []
print("hello {}\n{}".format(a,b))
hello oye
prasanna
print("hello\n{} {}".format(a,b))
hello
oye prasanna
#fstring
a="oye"
b="prasanna"
print(f"hello {a} {b}")
hello oye prasanna
print(f"hello\n{a} {b}")
hello
oye prasanna
a=3
b=2
c=a*b
print("product of{}",.format(c))
SyntaxError: invalid syntax
print("product of{}".format(c))
product of6
print("product of{}".format(a*b))
product of6
print(f"product of{c}")
product of6
