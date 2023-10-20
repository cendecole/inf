"""""
import random
n=3
a=list()
for i in range(n):
    b=list()
    for i in  range(n):
        b.append(int(round((random.random()*100),0)))
    a.append(b)
for i in range(n):
    for j in range(n):
        print(a[i][j], end =' ')
    print()
print(max(a[0][2],a[1][2],a[2][2]))
print(max(a[1][0],a[1][1],a[1][2]))

import random
from random import randint
n=(int(round((random.random()*10),0)))
m=(int(round((random.random()*10),0)))
a=list()
for i in range(n):
    b=list()
    for i in  range(m):
        b.append(randint(-100,100))
    a.append(b)
for i in range(n):
    for j in range(m):
        print(a[i][j], end =' ')
    print()
print('-'*10)
for i in range(n):
    for j in range(m):
        if a[i][j]>0:
            a[i][j]=1
        else:
            a[i][j]=0
for row in a:
  for element in row:
    print(element, end = ' ')
  print()
"""""
import random
from random import randint
n=(int(round((random.random()*10),0)))
a=list()
for i in range(n):
    b=list()
    for i in  range(n):
        b.append(randint(100))
    a.append(b)
for i in range(n):
    for j in range(n):
        print(a[i][j], end =' ')
    print()
for t in range(n):
    if(sum[n-n][])




















