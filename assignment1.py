Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = ["I'","work", "i", "Code"]
>>> b = ["am", "ing", "n", "gnan"]
>>> " ".join(a[0]+" "+b[0]+" "+a[1]+b[1]+" "+a[2]+b[2]+" "+a[3]+b[3])
"I '   a m   w o r k i n g   i n   C o d e g n a n"
>>> " ".join(a[0]+b[0]+" "+a[1]+b[1]+" "+a[2]+b[2]+" "+a[3]+b[3])
"I ' a m   w o r k i n g   i n   C o d e g n a n"
>>> " ".join([a[0]+" "+b[0]+" "+a[1]+b[1]+" "+a[2]+b[2]+" "+a[3]+b[3]])
"I' am working in Codegnan"
>>> a = ["I'","work", "i", "Code"]
>>> b = ["am", "ing", "n", "gnan"]
>>> " ".join([a[0]+" "+b[0]+" "+a[1]+b[1]+" "+a[2]+b[2]+" "+a[3]+b[3]])
"I' am working in Codegnan"
>>> a="silent"
>>> b=a.sort()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    b=a.sort()
AttributeError: 'str' object has no attribute 'sort'
>>> b = ''.join(sorted(a))
>>> b
'eilnst'
>>> a.reverse()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.reverse()
AttributeError: 'str' object has no attribute 'reverse'
>>> a="silent"
>>> b=a.replace("silent","listen")
>>> b=a.replace("\silent","listen")
>>> b
'silent'
>>> b=a.replace("silent\"for\"silent","listen")
>>> b
'silent'
