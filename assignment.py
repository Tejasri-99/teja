Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="pooja-is-Python-Mentor"
>>> b=a.spli("-")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    b=a.spli("-")
AttributeError: 'str' object has no attribute 'spli'. Did you mean: 'split'?
>>> a="pooja-is-Python-Mentor"
>>> b=a.split("-")
>>> b
['pooja', 'is', 'Python', 'Mentor']
>>> b=a.relace("-","' '").
SyntaxError: invalid syntax
>>> a = 'I work in Codegnan,and codegnan is in Vijayawada & I love codegnan'
>>> a.count("codegnan")
2
>>> a.count(" ")
11
>>> b=a.split()
>>> b.count("codegnan")
2
>>> a= "Ivis"; b="code"
>>> a = 'I work in Codegnan,and codegnan is in Vijayawada & I love codegnan'
>>> a.upper(c)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.upper(c)
NameError: name 'c' is not defined
>>> a= "Ivis"; b="code"
>>> c=a+b
>>> c
'Iviscode'
>>> c.split()
['Iviscode']
>>> c.pop()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    c.pop()
AttributeError: 'str' object has no attribute 'pop'
a = ["I'","work", "i", "Code"] 
b = ["am", "ing", "n", "gnan"]
SyntaxError: multiple statements found while compiling a single statement
a = ["I'","work", "i", "Code"]
b = ["am", "ing", "n", "gnan"]
" ".join()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    " ".join()
TypeError: str.join() takes exactly one argument (0 given)
" ".join(a[0]" "+b[0]" "+a[1]+a[1]" "+a[2]+b[2]" "+a[3]+b[3])
SyntaxError: invalid syntax. Perhaps you forgot a comma?
" ".join(a[0]," "+b[0]," "+a[1]+a[1]," "+a[2]+b[2]," "+a[3]+b[3])
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    " ".join(a[0]," "+b[0]," "+a[1]+a[1]," "+a[2]+b[2]," "+a[3]+b[3])
TypeError: str.join() takes exactly one argument (5 given)
" ".join(a[0]+" "+b[0]+" "+a[1]+a[1]+" "+a[2]+b[2]+" "+a[3]+b[3])
"I '   a m   w o r k w o r k   i n   C o d e g n a n"
" ".join(a[0]+""+b[0]+""+a[1]+b[1]+""+a[2]+b[2]+""+a[3]+b[3])
"I ' a m w o r k i n g i n C o d e g n a n"
" ".join(a[0]+""+b[0]+" "+a[1]+a[1]+" "+a[2]+b[2]+" "+a[3]+b[3])
"I ' a m   w o r k w o r k   i n   C o d e g n a n"
a = ('python','pooja',25,'codegnan',36,'mentor',[1,4,5],26)
b=a[2:4]
b
(25, 'codegnan')
b=a[1:2}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
b=a[1:2]
b
('pooja',)
b=a[1:2]+a[3:4]+a[5:6]+a[7:8]
b
('pooja', 'codegnan', 'mentor', 26)
a = ('python','pooja',25,'codegnan',36,'mentor',[1,4,5],26)
b=a[1:2]+a[3:4]+a[5:6]+a[7:8]
b
('pooja', 'codegnan', 'mentor', 26)
a="silent"
b="listen"
print(b)
listen
a.sort()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.sort()
AttributeError: 'str' object has no attribute 'sort'
a= "Ivis"
b="code"
a[0]+b[3]+a[1]+b[2]+a[2]+b[1]+a[3]+b[0]
'Ievdiosc'
a = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
a.split()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.split()
AttributeError: 'list' object has no attribute 'split'
a.pop()
'n'
type(a)
<class 'list'>
a.sort()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'list' and 'str'
a = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
a.sort()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'list' and 'str'
a.extend()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a.extend()
TypeError: list.extend() takes exactly one argument (0 given)
a.extend(a)
a
['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n', 'a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
a = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
a.extend(")
         
SyntaxError: unterminated string literal (detected at line 1)
a.extend(1)
         
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.extend(1)
TypeError: 'int' object is not iterable
a.extend(n)
         
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.extend(n)
NameError: name 'n' is not defined
a[2][1][2].extend(['h', 'i', 'j'])
         
a.extend(['h', 'i', 'j'])
         
b=a[2][1][2].extend(['h', 'i', 'j'])
         
b=a.extend(['h', 'i', 'j'])
         
a.extend(f)
         
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a.extend(f)
NameError: name 'f' is not defined
a = ["I'","work", "i", "Code"]
         
b = ["am", "ing", "n", "gnan"]
         
