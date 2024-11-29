Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
 #strip
#rstrip, #lstrip
a="     python     "
a.strip()
'python'
a.rstrip()
'     python'
a.lstrip()
'python     '
#concatenation
a="hello"
b="world"
print(a+b)
helloworld
print(a+" "+b)
hello world
#formatting
a=10
b=20
print(a+b)
30
print("the sum is",a+b)
the sum is 30
print("the sum is,a+b")
the sum is,a+b
a="teja"
b="sri"
>>> print("my full name is",a+b)
my full name is tejasri
>>> #.format
>>> a="sita"
>>> b="ram"
>>> print("hello {} {}".format(a,b))
hello sita ram
>>> print("hello {}{}".format(a+b))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print("hello {}{}".format(a+b))
IndexError: Replacement index 1 out of range for positional args tuple
>>> print("hello {}{}".format(a,b))
hello sitaram
>>> print("hello {} hello {}".format(a,b))
hello sita hello ram
>>> #fstring
>>> a="motu"
>>> b="patlu"
>>> print(f"hello {a}{b}")
hello motupatlu
>>> print(f"hello {a} {b}")
hello motu patlu
>>> print(f"hello{a} hello{b}")
hellomotu hellopatlu
>>> print(f"hello {a} hello {b}")
hello motu hello patlu
