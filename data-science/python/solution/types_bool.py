a = bool(False)
b = bool(True)

c = bool('a')
d = bool('.')
e = bool('0')
f = bool('0.0')
g = bool('')
h = bool(' ')

i = bool(0)
j = bool(0.0)
k = bool(-0)
l = bool(-0.0)

m = bool(int('0'))
n = bool(float('-0'))

o = bool(-0.0+0.0j)
p = bool('-0.0+0.0j')


print(a)    # False
print(b)    # True
print(c)    # True
print(d)    # True
print(e)    # True
print(f)    # True
print(g)    # False
print(h)    # True
print(i)    # False
print(j)    # False
print(k)    # False
print(l)    # False
print(m)    # False
print(n)    # False
print(o)    # False
print(p)    # True
