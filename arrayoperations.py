from array import *

a = array('d',[10.53,21.25,-3,40,5,6])
print(a)

for element in a:
    print(element)


b = array('u',['a','b','c','d'])
print(b)

c= array('i',[11,22,23,33])
print(c[1:3])
print(c[:-1])

c.append(110)
print(c)

print(c.index(110))
print(c.index(22,1,3))
print(c.count(22))
x= array('i',[25,35,26,58,25])
c.extend(x)
print(c)

c.fromlist([11,22])
print(c)

print(c.pop())
c.remove(11)
print(c)
c.reverse()
print(c)

l=c.tolist()
print(l)

x= array('u',['a','b','c'])
print(x.typecode)
print(x.itemsize)