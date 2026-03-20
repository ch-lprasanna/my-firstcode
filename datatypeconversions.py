Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatype conversions
>>> #int
>>> int(90)
90
>>> int(9.0)
9
>>> int(3+6j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(3+6j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int("str")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int("str")
ValueError: invalid literal for int() with base 10: 'str'
>>> int(True)
1
>>> int(False)
0
>>> #float
>>> float(2)
2.0
>>> float)2.3)
SyntaxError: unmatched ')'
>>> float(2.3)
2.3
>>> float("str")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float("str")
ValueError: could not convert string to float: 'str'
>>> float(3+5j)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    float(3+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> flase(False)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    flase(False)
NameError: name 'flase' is not defined
float(False)
0.0
#str
str(2)
'2'
str(2.3)
'2.3'
str("str)
    
SyntaxError: unterminated string literal (detected at line 1)
str("str")
    
'str'
str("hi")
    
'hi'
str(hi)
    
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    str(hi)
NameError: name 'hi' is not defined
str("boolean")
    
'boolean'
str("boolean")
    
'boolean'
str(3+6j)
    
'(3+6j)'
str(True)
    
'True'
str(False)
    
'False'
#complex
    
comp(3)
    
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    comp(3)
NameError: name 'comp' is not defined
complex(3)
    
(3+0j)
complex(3.4)
    
(3.4+0j)
complex("str")
    
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    complex("str")
ValueError: complex() arg is a malformed string
complex(3+4j)
    
(3+4j)
complex(True)
    
(1+0j)
complex(False)
    
0j
#bool
    
bool(3)
    
True
bool(3.4)
    
True
bool("str")
    
True
bool(3+6j)
    
True
bool(True)
    
True
bool(False)
    
False
