Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
 #sets
a={4,6.7,"pooja",7+9j,True,False}
print(a)
{False, True, (7+9j), 4, 6.7, 'pooja'}
type(a)
<class 'set'>
b={6,8,4,7,2,0,1}
print(a)
{False, True, (7+9j), 4, 6.7, 'pooja'}
type(a)
<class 'set'>
print(b)
{0, 1, 2, 4, 6, 7, 8}
#methods in sets
a={2,5,7,9,11}
a.add(20)
a
{2, 20, 5, 7, 9, 11}
a.add(15)
a
{2, 20, 5, 7, 9, 11, 15}
a={2,5,8,3,0}
a.add(10)
a
{0, 2, 3, 5, 8, 10}
#issubset()
a={1,2,3,4,5,6,7}
b={5,6,7}
a.issubset(b)
False
b.issubset(a)
True
#issuperset()
a.issuperset(b)
True
b.issuperset(a)
False
#union()
a={1,2,3,4,5,6}
b={4,5,6,7,8,9}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
#intersection()
a={3,4,5,6,7,8,9}
b
{4, 5, 6, 7, 8, 9}
b={6,7,8,9,11,12}
a,intersection(b)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a,intersection(b)
NameError: name 'intersection' is not defined
a.intersection(b)
{8, 9, 6, 7}
a={2,4,6,8,10,12,14}
b={1,3,5,6,8,10,14}
a.difference(b)
{2, 4, 12}
b.difference(a)
{1, 3, 5}
#update()
a={1,2,3,4,5,6,7}
b={4,5,6,7,8,9,10,11}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
#difference_update
a={2,3,4,5,6,7,8}
b={5,6,7,8,9,10}
a.difference_update(b)
a
{2, 3, 4}
b.difference_update9a)
SyntaxError: unmatched ')'
b.difference_update(a)
b
{5, 6, 7, 8, 9, 10}
 #symmetric_difference
a={1,2,3,4,5,6,7}
b={3,4,5,6,9,11}
a.symmetric_difference(b)
{1, 2, 7, 9, 11}
b.symmetric_difference(a)
{1, 2, 7, 9, 11}
#intersection_update
a={1,2,3,4,5,6,7}
b={9,5,6,7,8}
a.intersection_update(b)
a
{5, 6, 7}
b.intersection_update(a)
b
{5, 6, 7}
#symmetric_difference_update
a={2,3,4,5,0,1,10}
b={4,5,6,7,8,9}
a.symmetric_difference_update(b)
a
{0, 1, 2, 3, 6, 7, 8, 9, 10}
b.symmetric_difference_update(a)
b
{0, 1, 2, 3, 4, 5, 10}
a
{0, 1, 2, 3, 6, 7, 8, 9, 10}
b
{0, 1, 2, 3, 4, 5, 10}
#remove()
a={11,12,13,14,15,16}
b={14,15,16,17,18,19}
a.remove(11)
a
{16, 12, 13, 14, 15}
#pop()
a.pop()
16
a.pop(12)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a.pop(12)
TypeError: set.pop() takes no arguments (1 given)
>>> #copy()
>>> a={2,3,4,5,6,7,8}
>>> a.copy()
{2, 3, 4, 5, 6, 7, 8}
>>> #clear()
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(40)
>>> a
set()
>>> b.add(60,70)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    b.add(60,70)
TypeError: set.add() takes exactly one argument (2 given)
>>> #discard()
>>> a={1,2,3,4,5,6}
>>> b={6,7,8,9,10}
>>> a.discard(1)
>>> a
{2, 3, 4, 5, 6}
