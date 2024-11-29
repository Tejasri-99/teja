Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="cost of the apple is 30rs and cost of the orange is 45rs"
>>> print("total cost of the fruits ")
total cost of the fruits 
>>> print("total cost of the fruits is 75rs")
total cost of the fruits is 75rs
>>> a[-54:-35]
'st of the apple is '
>>> a[-33:-31]
'rs'
>>> a=[123,"abc",123,"abc","calm"]
>>> b=[{set(a)}]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    b=[{set(a)}]
TypeError: unhashable type: 'set'
>>> b=set(a)
>>> list(b)
['abc', 'calm', 123]
>>> b=list(set(a))
>>> b
['abc', 'calm', 123]
>>>  a="abracadabra@magic!!!@?"
...  
SyntaxError: unexpected indent
>>> a="abracadabra@magic!!!@?"
>>> a.split()
['abracadabra@magic!!!@?']
a="abracadabra @ magic !!! @ ?"
a.spli()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.spli()
AttributeError: 'str' object has no attribute 'spli'. Did you mean: 'split'?
a.split()
['abracadabra', '@', 'magic', '!!!', '@', '?']
a.remove("@","!!!","?")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.remove("@","!!!","?")
AttributeError: 'str' object has no attribute 'remove'
b=list(a)
b
['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a', ' ', '@', ' ', 'm', 'a', 'g', 'i', 'c', ' ', '!', '!', '!', ' ', '@', ' ', '?']
a="abracadabra@magic!!!@?"
b=list(a)
b
['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a', '@', 'm', 'a', 'g', 'i', 'c', '!', '!', '!', '@', '?']
a="abracadabra @ magic !!! @ ?"
b=list(a)
b
['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a', ' ', '@', ' ', 'm', 'a', 'g', 'i', 'c', ' ', '!', '!', '!', ' ', '@', ' ', '?']
b=set(a)
b
{'i', 'a', '@', '!', 'm', '?', 'd', 'b', 'r', ' ', 'c', 'g'}
a="abracadabra @ magic !!! @ ?"
a.split()
['abracadabra', '@', 'magic', '!!!', '@', '?']
a[:]
'abracadabra @ magic !!! @ ?'
a[:2]
'ab'
b=int(a[1])+int(a[3])
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    b=int(a[1])+int(a[3])
ValueError: invalid literal for int() with base 10: 'b'
b=int a(1)+ int a(3)
SyntaxError: invalid syntax
int a[:2]
SyntaxError: invalid syntax
ab=a.split(a)
ab
['', '']
a="abracadabra @ magic !!! @ ?"
b=a.split(a)
b
['', '']
a="java @ %
SyntaxError: unterminated string literal (detected at line 1)
a="java @ %"
b=a.split()
b
['java', '@', '%']
a="abracadabra @ magic !!! @ ?"
b=a.split()
b
['abracadabra', '@', 'magic', '!!!', '@', '?']
b[:2]
['abracadabra', '@']
b[1:3]
['@', 'magic']
a.remove("@")
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.remove("@")
AttributeError: 'str' object has no attribute 'remove'
c=list(b)
c
['abracadabra', '@', 'magic', '!!!', '@', '?']
c.remove("@")
c
['abracadabra', 'magic', '!!!', '@', '?']
c.remove("!!!","@","?")
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    c.remove("!!!","@","?")
TypeError: list.remove() takes exactly one argument (3 given)
c.remove("!!!")
c
['abracadabra', 'magic', '@', '?']
c.remove("@")
c
['abracadabra', 'magic', '?']
c.remove("?")
c
['abracadabra', 'magic']
d=str(c)
d
"['abracadabra', 'magic']"
a = "Python learning am I"
b=a_string.split()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    b=a_string.split()
NameError: name 'a_string' is not defined
b=input_string.split()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    b=input_string.split()
NameError: name 'input_string' is not defined
b=a.split()
b
['Python', 'learning', 'am', 'I']
b.reverse()
b
['I', 'am', 'learning', 'Python']
string(b)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    string(b)
NameError: name 'string' is not defined
c=str(b)
c
"['I', 'am', 'learning', 'Python']"
c="".join(b)
c
'IamlearningPython'
c=" ".join(b)
c
'I am learning Python'
a = "Python learning am I"
a.split()
['Python', 'learning', 'am', 'I']
a.reverse()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.reverse()
AttributeError: 'str' object has no attribute 'reverse'
a = "Python learning am I"
c=a.split()
c.reverse()
b=" ".join(c)
b
'I am learning Python'
a = "Python learning am I"
c=a.split()
c
['Python', 'learning', 'am', 'I']
c.reverse()
c
['I', 'am', 'learning', 'Python']
" ".join()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    " ".join()
TypeError: str.join() takes exactly one argument (0 given)
" ".join(c)
'I am learning Python'
a = "Python learning am I"
b=a.split()
b
['Python', 'learning', 'am', 'I']
b.reverse()
b
['I', 'am', 'learning', 'Python']
" ".join(b)
'I am learning Python'
a="pooja-is-Python-Mentor"
b=a.split()
b
['pooja-is-Python-Mentor']
a.replace("'")
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    a.replace("'")
TypeError: replace expected at least 2 arguments, got 1
a.replace("-","'")
"pooja'is'Python'Mentor"
b=a.split()
b
['pooja-is-Python-Mentor']
b.replace("-","'")
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    b.replace("-","'")
AttributeError: 'list' object has no attribute 'replace'
b=a.replace("-","'")
b
"pooja'is'Python'Mentor"
b.split()
["pooja'is'Python'Mentor"]
a="pooja-is-Python-Mentor"
b=a.replace("-","'")
b
"pooja'is'Python'Mentor"
b.split()
["pooja'is'Python'Mentor"]
b=a.replace("-","' '")
b
"pooja' 'is' 'Python' 'Mentor"
b=a.split()
b
['pooja-is-Python-Mentor']
b.replace("-","'")
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    b.replace("-","'")
AttributeError: 'list' object has no attribute 'replace'
b=a.replace("-","' '".split()
            b
            
SyntaxError: '(' was never closed
b=a.replace("-","' '").split()
            
b=a.split("-")
            
b
            
['pooja', 'is', 'Python', 'Mentor']
a="pooja-is-Python-Mentor"
            
a="pooja-is-Python-Mentor"
            
b=a.replace("-","'").replace(""","'")
