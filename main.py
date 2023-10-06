i=int(input("введите верхний предел:"))
a=1
b=0
if i>100:
    print("ошибка!")
else:
    while a<i:
        b=b+a*a*a
        a=a+1
    print(b)


















