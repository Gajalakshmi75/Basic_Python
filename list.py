Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3,4,5,6,7,8,9]
>>> print(l)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print(l[7])
8
>>> print(l[-5])
5
>>> l[0]=0
>>> print(l)
[0, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print(l[:7])
[0, 2, 3, 4, 5, 6, 7]
>>> print(l[0:])
[0, 2, 3, 4, 5, 6, 7, 8, 9]
>>> len(l)
9
>>> l.extend([10,11])
>>> len(l)
11
>>> print(l)
[0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> l.append([12,13,14])
>>> print(l)
[0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, [12, 13, 14]]
>>> l.insert(0,1)
>>> l
[1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, [12, 13, 14]]
>>> print(l[12])
[12, 13, 14]
>>> l.remove(1)
>>> l
[0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, [12, 13, 14]]
>>> l.remove(2)
>>> l
[0, 3, 4, 5, 6, 7, 8, 9, 10, 11, [12, 13, 14]]
>>> del(l[0])
>>> l
[3, 4, 5, 6, 7, 8, 9, 10, 11, [12, 13, 14]]
>>> l[1:3]=[0,1,2]
>>> l
[3, 0, 1, 2, 6, 7, 8, 9, 10, 11, [12, 13, 14]]
>>> del(l[10])
>>> l
[3, 0, 1, 2, 6, 7, 8, 9, 10, 11]
>>> l.sort()]
SyntaxError: unmatched ']'
>>> l.sort()
>>> l
[0, 1, 2, 3, 6, 7, 8, 9, 10, 11]
>>> l.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    l.sort(reverse=true)
NameError: name 'true' is not defined
>>> l.sort(reverse=True)
>>> print(l)
[11, 10, 9, 8, 7, 6, 3, 2, 1, 0]
>>> m=l
>>> l
[11, 10, 9, 8, 7, 6, 3, 2, 1, 0]
>>> m
[11, 10, 9, 8, 7, 6, 3, 2, 1, 0]
>>> 