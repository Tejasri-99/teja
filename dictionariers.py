Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  #dict{}
>>> a={"name":"pooja","year":2024,"month":10}
>>> print(a)
{'name': 'pooja', 'year': 2024, 'month': 10}
>>> type(a)
<class 'dict'>
>>> b={4,5,6,7,8,9}
>>> print(b}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> print(b)
{4, 5, 6, 7, 8, 9}
>>> type(b)
<class 'set'>
>>> print(a)
{'name': 'pooja', 'year': 2024, 'month': 10}
>>> type(a)
<class 'dict'>
>>> 
...  
>>> #methods in dictionary
>>> a={"name":"pooja","year":2024,"month":10}
>>> a.keys()
dict_keys(['name', 'year', 'month'])
>>> a.values()
dict_values(['pooja', 2024, 10])
>>> a.items()
dict_items([('name', 'pooja'), ('year', 2024), ('month', 10)])
>>> a["course"]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a["course"]
KeyError: 'course'
>>> a["name"]
'pooja'
>>> a["year"]
2024
#accessing items
#it will remove duplicate values

#copy()
a={"name":"pooja","date":29,"month":"oct","time":12,"year":2024,"course":"python","place":"vij"}
a.copy()
{'name': 'pooja', 'date': 29, 'month': 'oct', 'time': 12, 'year': 2024, 'course': 'python', 'place': 'vij'}
a={"name":"pooja","date":29,"month":"oct","time":12,"year":2024,"course":"python","place":"vij"}
a.update({"institute":"codegnan"})
a
{'name': 'pooja', 'date': 29, 'month': 'oct', 'time': 12, 'year': 2024, 'course': 'python', 'place': 'vij', 'institute': 'codegnan'}
a.update({"institute":"codegnan"},{"joining":"nov"})
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.update({"institute":"codegnan"},{"joining":"nov"})
TypeError: update expected at most 1 argument, got 2
a.update({"institute":"codegnan","joining":"nov"})
a
{'name': 'pooja', 'date': 29, 'month': 'oct', 'time': 12, 'year': 2024, 'course': 'python', 'place': 'vij', 'institute': 'codegnan', 'joining': 'nov'}

a={"year":2025,"month":1}
a.setdefault("name","pooja")
'pooja'
a
{'year': 2025, 'month': 1, 'name': 'pooja'}
 a.update("year",2026)
 
SyntaxError: unexpected indent
a.update("year",2026)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.update("year",2026)
TypeError: update expected at most 1 argument, got 2
a.update({"year":2026})
a
{'year': 2026, 'month': 1, 'name': 'pooja'}

#popitem
a={"course":"python","place":"codegnan"}
a.popitem()
('place', 'codegnan')
a.pop("place")
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.pop("place")
KeyError: 'place'
a
{'course': 'python'}
a.get("course")
'python'
a.pop("place")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.pop("place")
KeyError: 'place'
a.pop("course")
'python'
a
{}
 a.clear{}
 
SyntaxError: unexpected indent
a.clear()
a
{}
b={"course":"python","place":"codegnan"}
b.copy()
{'course': 'python', 'place': 'codegnan'}
