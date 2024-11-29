Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#list
a=[2,4.5,"python",8+9j,True,False]
type(a)
<class 'list'>
b=4.5
type(b)
<class 'float'>
b=[4.5]
type(b)
<class 'list'>
a=["python", "java", "c", "c++"]
type(a)
<class 'list'>
#append()
a.append("html")
a
['python', 'java', 'c', 'c++', 'html']
a.append("css", "js")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.append("css", "js")
TypeError: list.append() takes exactly one argument (2 given)
#extend
a=["ds","ai","ml"]
a.extend("java","python")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.extend("java","python")
TypeError: list.extend() takes exactly one argument (2 given)
a.extend(["java","python","vzg"])
a.insert(1,"chennai")
a
['ds', 'chennai', 'ai', 'ml', 'java', 'python', 'vzg']
#insert()
a=["vja","hyd","beng","vzg"]
a.insert(3,"ooty")
a
['vja', 'hyd', 'beng', 'ooty', 'vzg']

 
a=["apple","banana","grapes"]
a
['apple', 'banana', 'grapes']
a.index("apple")
0
#reverse()
a.reverse()
a
['grapes', 'banana', 'apple']
#sort()
a=["java","css",".net","python","c"]
a.sort()
a
['.net', 'c', 'css', 'java', 'python']
b=[8,0,2,4,6,15,1]
b.reverse()
b
[1, 15, 6, 4, 2, 0, 8]
b.sort()
b
[0, 1, 2, 4, 6, 8, 15]


a=["code","codegnan","course"]
a.remove("code"
         a
         
SyntaxError: '(' was never closed
a
         
['code', 'codegnan', 'course']
a.remove9"code)
         
SyntaxError: unterminated string literal (detected at line 1)
a.remove("code")
         
a
         
['codegnan', 'course']
#pop()
         
a.pop()
         
'course'
a
         
['codegnan']
a.pop(0)
         
'codegnan'
a.pop(1)
         
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.pop(1)
IndexError: pop from empty list

a=["ml","ai","ds","python"]
         
a.copy()
         
['ml', 'ai', 'ds', 'python']
#clear()
         
a.clear()
         
a
         
[]
b=[]
         
b.append("hi"
         b
         
SyntaxError: '(' was never closed
b
         
[]

a="python"
         
len(a)
         
6
b==["python"]
         
False
b=["python"]
         
len(b)
         
1
a=["python","java","c","c++"]
         
a.count("java")
         
1
len(a)
         
4
a=["python,java,c,c++"]
         
len(a)
         
1
 #tuple()
         
a==(4,6.5,"class",5+8j,True,false)
         
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a==(4,6.5,"class",5+8j,True,false)
NameError: name 'false' is not defined. Did you mean: 'False'?
Type(a)
         
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    Type(a)
NameError: name 'Type' is not defined. Did you mean: 'type'?
a=(4,6.5,"class",5+8j,True,false)
         
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a=(4,6.5,"class",5+8j,True,false)
NameError: name 'false' is not defined. Did you mean: 'False'?
a=(4,6.5,"class",5+8j,True,False)
         
Type9a)
         
SyntaxError: unmatched ')'
Type(a)
         
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    Type(a)
NameError: name 'Type' is not defined. Did you mean: 'type'?
type(a)
         
<class 'tuple'>
a.count(6.5)
         
1
len(a)
         
6
a.index(5+8j)
         
3
>>> a.revese()
...          
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a.revese()
AttributeError: 'tuple' object has no attribute 'revese'
>>> a.reverse()
...          
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
>>> a.sort()
...          
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> a=(4,6.5,"class",5+8j,True,False)
...          
>>> a.sort()
...          
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    a.sort()
AttributeError: 'tuple' object has no attribute 'sort'
