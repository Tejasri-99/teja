Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="code"
len(a)
4
a="computer"
len(a)
8
b=" "
len(b)
1
c=""
len(c)
0
#count
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count(" ")
3
a.count("e")
3
a.count("T")
0
#find a string
 a="ptthon course"
 
SyntaxError: unexpected indent
a="python course"
a.find(" ")
6
a.find("r")
10
a="i am in class"
a.find("i")
0
a.find("")
0
a.find("in")
5
a.find("class")
8
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
a.replace("wait","work",2)
'work until you succeed'
a="people never change their habbits"
a.replace("never","will never")
'people will never change their habbits'
>>> #escape sequences
>>> a="name\nmobileno\tmailid\naddress
SyntaxError: unterminated string literal (detected at line 1)
>>> a="name\nmobileno\tmailid\naddress"
>>> print(a)
name
mobileno	mailid
address
>>> a="ammu\nmobileno:8623543616\tmailid:teja@gmail.com"
>>> print(a)
ammu
mobileno:8623543616	mailid:teja@gmail.com
>>> #upper
>>> a="hello"
>>> a.upper()
'HELLO'
>>> #lower
>>> b="HI"
>>> b.lower()
'hi'
>>> #capitalise
>>>  a="python"
...  
SyntaxError: unexpected indent
>>> a="python"
>>> a.capitalize()
'Python'
