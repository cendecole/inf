"""""
from random import randint
l = [randint(10, 80) for x in range(10)]
print(l)
def pr(a):
    l=a[0],a[-1]=a[-1],a[0]
    return a
print(pr(l))


import math
l = [6,12,5,15]
a=l[0]*l[3]
b=l[1]*l[2]
if b==0:
    print('fail')
c=math.gcd(a, b)
if b==1:
    print(int(a/c))
else:
    print(int(a/c),'/',int(b/c))
"""""
x=int(input('x='))
y=int(input('y='))
r=int(input('r='))
if r^2!=x^2+y^2:
    print('fail')






















