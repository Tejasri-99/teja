Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#operators
1.arithmetic
SyntaxError: invalid decimal literal
#arithmetic
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a//b)
0
print(a/b)
0.5
print(a%b)
2
print(b%a)
0
print(b//a)
2

print(a/b)
0.5
print(b/a)
2.0
#assignment
a=2
b=4
a+=4
a
6
a-=b
a
2
a*=6
a
12
a//=5
a
2
a/=b
a
0.5
a%=b

a
0.5
a%=b
a
0.5
print(a**b)
0.0625
a**=b
a
0.0625
#comparison
a=5
b=7
a<b
True
a>b
False
a<=b
True
a>=b
False
a!=b
True
a==b
False
#logical
a=4
b=8
a==b and a!=b
False
a==b or a!=b
True
a<b or a>b
True
not True
False
#identify
a=4.5
if type(a)is float:
    print("true"
          else:
              
SyntaxError: '(' was never closed
print("true")
true
print("false")
false
if type(a)is float:
    print("true")
    else:
        
SyntaxError: invalid syntax
else:
    
SyntaxError: invalid syntax
      print("false")
      
SyntaxError: unexpected indent
else:
    
SyntaxError: invalid syntax
#identify
a=4.5
if type(a) is float:
    print("true")
    else:
        
SyntaxError: invalid syntax
else:
    
SyntaxError: invalid syntax
a=4.5
if type(a) is float:
    print(True)
else:
    print(False)

    
True
b=4
if type(b)is not float:
    print("true")
else:
    print("false")

    
true
if type(a) is not float:
    print("true")
else:
...     print("false")
... 
...     
false
>>> #membership
>>> a=2,4,6,8,10
>>> if 10 in a:
...     print(10)
... 
...     
10
>>> if 20 in a:
...     print(20)
... 
...     
>>> if 20 is not in a:
...     
SyntaxError: invalid syntax
>>> if 20 not in a:
...     print(20)
... 
...     
20
>>> if 10 not in a:
...     print(10)
... 
...     
