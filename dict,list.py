Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a={"name":"ammu","year":2003,"course":"python"}
a.items()
dict_items([('name', 'ammu'), ('year', 2003), ('course', 'python')])
#single key assign no.f values
>>> a={"idnos":[10,20,30,],"names":["manikanta","rajesh","yogeswar"]}
>>> print(a)
{'idnos': [10, 20, 30], 'names': ['manikanta', 'rajesh', 'yogeswar']}
>>> type(a)
<class 'dict'>
>>> a={"idnos":10,20,30,,"names":["manikanta","rajesh","yogeswar"]}
SyntaxError: ':' expected after dictionary key
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a.sort()
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a[8]
7
>>> a[8]+a[6]+a[5]+a[7]+a[9]+a[0]+a[4]+a[2]+a[3]+a[1]
45
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> b=a[:5]
>>> b
[9, 1, 5, 2, 8]
>>> c=a[5:]
>>> c
[4, 6, 3, 7, 0]
>>> b.sort()
>>> b
[1, 2, 5, 8, 9]
>>> c.sort()
>>> c
[0, 3, 4, 6, 7]
>>> b.reverse()
>>> b
[9, 8, 5, 2, 1]
>>> c.reverse()
>>> c
[7, 6, 4, 3, 0]
>>> c+b
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
