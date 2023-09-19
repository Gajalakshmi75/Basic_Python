Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s="python is very fun subject"
>>> s.partitoin("is")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s.partitoin("is")
AttributeError: 'str' object has no attribute 'partitoin'
>>> s.partition("is")
('python ', 'is', ' very fun subject')
>>> s="python is fun"
>>> s.partition("is")
('python ', 'is', ' fun')
>>> s1="rajiv gandhi university of knowledge technologies"
>>> s1.partition("of")
('rajiv gandhi university ', 'of', ' knowledge technologies')
>>> tuple=("lakshmi","cool","chinni")
>>> x="*".join(tuple)
>>> print(x)
lakshmi*cool*chinni
>>> s1="abc"
>>> s2="123"
>>> s2.join(s1)
'a123b123c'
>>> s1.join(s2)
'1abc2abc3'
>>> s="chinni","gaja lakshmi"
>>> s.replace("gaja","maha")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s.replace("gaja","maha")
AttributeError: 'tuple' object has no attribute 'replace'
>>>  s="chinni,gaja lakshmi"
 
SyntaxError: unexpected indent
>>> s="chinni,gaja lakshmi"
>>> s.replace("gaja","maha")
'chinni,maha lakshmi'
>>> s.replace("gaja","maha",2)
'chinni,maha lakshmi'
>>> s="grapes,apples,mangoes"
>>> s.split()
['grapes,apples,mangoes']
>>> s="chicken is my fav food"
>>> s.split()
['chicken', 'is', 'my', 'fav', 'food']
>>> s="rgukt SKLM iiit"
>>> s.swapcase()
'RGUKT sklm IIIT'
>>> s='LAKSHMI"
SyntaxError: EOL while scanning string literal
>>> s="LAKSHMI"
>>> s.lower()
'lakshmi'
>>> 