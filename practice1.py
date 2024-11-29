Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
a.extend("")
a
['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']

a = 'I work in Codegnan,and codegnan is in Vijayawada & I love codegnan'
a.count("Codegnan")
1
a.tittle()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.tittle()
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
a.title()
'I Work In Codegnan,And Codegnan Is In Vijayawada & I Love Codegnan'
a.count("
KeyboardInterrupt
a.count("Codegnan")
        
1
a.upper("c")
        
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.upper("c")
TypeError: str.upper() takes no arguments (1 given)
a.capitalize("codegnan")
        
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.capitalize("codegnan")
TypeError: str.capitalize() takes no arguments (1 given)
capatilize("codegnan")
        
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    capatilize("codegnan")
NameError: name 'capatilize' is not defined
b=a.capatilize()
        
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    b=a.capatilize()
AttributeError: 'str' object has no attribute 'capatilize'. Did you mean: 'capitalize'?
b=a.capatilize("codegnan")
        
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    b=a.capatilize("codegnan")
AttributeError: 'str' object has no attribute 'capatilize'. Did you mean: 'capitalize'?
a[11:12]
        
'o'
a[10:11]
        
'C'
KeyboardInterrupt
a[45:46]
        
'a'
a[44:45]
        
'w'
a[57:58]
        
' '
a[56:57]
        
'e'
a[46:47]
        
'd'
a[57:58]
        
' '
a[58:59]
        
'c'
a[10:11]+a[58:59].capitalize()
        
'CC'
a
        
'I work in Codegnan,and codegnan is in Vijayawada & I love codegnan'
a = 'I work in Codegnan,and codegnan is in Vijayawada & I love codegnan'
        
a = 'I work in Codegnan,and codegnan is in Vijayawada & I love codegnan'
        
count = a.lower().count('codegnan')
        
print(count)
        
3
count
        
3
a = 'I work in Codegnan,and codegnan is in Vijayawada & I love codegnan'
        
b=a.lower()
        
b
        
'i work in codegnan,and codegnan is in vijayawada & i love codegnan'
b.count("codegnan")
        
3
a = ["I'","work", "i", "Code"]
        
b = ["am", "ing", "n", "gnan"]
        
" ".join([a[0]+" "+b[0]+" "+a[1]+b[1]+" "+a[2]+b[2]+" "+a[3]+b[3]])
        
"I' am working in Codegnan"
" ".join(a[0]+" "+b[0]+" "+a[1]+b[1]+" "+a[2]+b[2]+" "+a[3]+b[3])
        
"I '   a m   w o r k i n g   i n   C o d e g n a n"
" ".join[(a[0]+" "+b[0]+" "+a[1]+b[1]+" "+a[2]+b[2]+" "+a[3]+b[3])]
        
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    " ".join[(a[0]+" "+b[0]+" "+a[1]+b[1]+" "+a[2]+b[2]+" "+a[3]+b[3])]
TypeError: 'builtin_function_or_method' object is not subscriptable
c=" ".join([a[0]+" "+b[0]+" "+a[1]+b[1]+" "+a[2]+b[2]+" "+a[3]+b[3]])
        
c
        
"I' am working in Codegnan"
type(c)
        
<class 'str'>
list(c)
        
['I', "'", ' ', 'a', 'm', ' ', 'w', 'o', 'r', 'k', 'i', 'n', 'g', ' ', 'i', 'n', ' ', 'C', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
c=a+b
        
c
        
["I'", 'work', 'i', 'Code', 'am', 'ing', 'n', 'gnan']
c[0+" "+c[5]+" "+a[2]+a[6]+" "+a[3]+a[7]+" "+c[4]+c[8]
  c
  
SyntaxError: '[' was never closed
" ".join([c[0+" "+c[5]+" "+a[2]+a[6]+" "+a[3]+a[7]+" "+c[4]+c[8]])
         
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
" ".join([c[0]+" "+c[5]+" "+c[2]+c[6]+" "+c[3]+c[7]+" "+c[4]+c[8]])
         
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    " ".join([c[0]+" "+c[5]+" "+c[2]+c[6]+" "+c[3]+c[7]+" "+c[4]+c[8]])
IndexError: list index out of range
c[0]
         
"I'"
c[1]
         
'work'
c[2]
         
'i'
c[3]
         
'Code'
c[4]
         
'am'
c[5]
         
'ing'
c[6]
         
'n'
c[7]
         
'gnan'
c[8]
         
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    c[8]
IndexError: list index out of range
" ".join([c[0]+" "+c[4]+" "+c[1]+c[5]+" "+c[2]+c[6]+" "+c[3]+c[7]])
         
"I' am working in Codegnan"
>>> d=" ".join([c[0]+" "+c[4]+" "+c[1]+c[5]+" "+c[2]+c[6]+" "+c[3]+c[7]])
...          
>>> d
...          
"I' am working in Codegnan"
>>> list(d)
...          
['I', "'", ' ', 'a', 'm', ' ', 'w', 'o', 'r', 'k', 'i', 'n', 'g', ' ', 'i', 'n', ' ', 'C', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
>>> a = ["I'","work", "i", "Code"]
...          
>>> b = ["am", "ing", "n", "gnan"]
...          
>>> c=a+b
...          
>>> c
...          
["I'", 'work', 'i', 'Code', 'am', 'ing', 'n', 'gnan']
>>> " ".join([c[0]+" "+c[4]+" "+c[1]+c[5]+" "+c[2]+c[6]+" "+c[3]+c[7]])
...          
"I' am working in Codegnan"
>>> " ".join([c[0]+" "+c[4]+" "+c[1]+c[5]+" "+c[2]+c[6]+" "+c[3]+c[7]]).split()
...          
["I'", 'am', 'working', 'in', 'Codegnan']
>>> a="silent"
...          
>>> b=a.replace("silent","listen").str()
...          
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    b=a.replace("silent","listen").str()
AttributeError: 'str' object has no attribute 'str'
>>> str=a.replace("silent","listen")
...          
>>> str
...          
'listen'
>>> type(str)
...          
<class 'str'>
