a=('dog','cat','elephant','ant')
print(a)
print(type(a))
print(len(a))
print(a[0])
x=(1j,)
print(type(x))
b=tuple((1,2,3,4,5))
print(b)
print(b[0:3])
print(b[:4])
print(b[1:])
print(b[-3:-1])
print(b[:-1])
print(3 in b)
print(7 not in b)
c=list(b)
print(c)
c[4]=6
print(c)
y=tuple(c)
print(y)
for i in b:
    print(i)
z=a+b
print(z)
w=(10,20)
h=w*2
print(h)
print(h.count(10))