#for a in range(1040,1072,5):
    #print('-'*20)
    #print('|',chr(a),chr(a+32),'||',chr(a+1),chr(a+33),'||',chr(a+2),chr(a+34),'||',chr(a+3),chr(a+35),'||',chr(a+4),chr(a+36),'|')
    #a=a+5

#import math
#a=int(input("введите радиус в сантиметрах:"))
#print(round(2*math.pi*a,2),round(math.pi*math.pi*a),2)

#y=55
#x=10
#print(x,y)
#x,y=y,x
#print(x,y)

#import math
#l=int(input("введите длину маятника:"))
#t=2*math.pi*math.sqrt(l/9.81)
#print(round(t,2))

#a=int(input("введите делимое:"))
#b=int(input("введите делитель:"))
#if b==0:
#    print("Ошибка! Деление на 0!")
#else:
#    print(a/b)

#i=int(input("введите стоимость в рублях:"))
#if i>20:
#    print(round((i/100)*65,2),"скидка:",round((i/100)*35,2))
#else:
#    print(i)

#a=['январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь']
#i=int(input("введите число:"))
#if i<1 or i>12:
#    print("ошибка!")
#else:
#    print(a[i-1])

#i=int(input("введите верхний предел:"))
#a=1
#b=0
#if i>100:
#    print("ошибка!")
#else:
#    while a<i:
#        b=b+a*a*a
#        a=a+1
#    print(b)



##############################################################################################

#n='Дана строка. Подсчитать самую длинную последовательность подряд идущих букв «н». Преобразовать ее, заменив точками все восклицательные знаки.'
#print(n.count(' Е')+n.count(' е'))

#n='Примеры: Ничего не было видно: была безумная ночь.'
#i=0
#while ':' in n:
#    n=n.replace(':','%',1)
#    i=i+1
#print(i)

#n='Дана строка, содержащая русскоязычный текст. Найти количество слов, начинающихся с буквы "е".'
#i=0
#while '.' in n:
#    n=n.replace('.','',1)
#    i=i+1
#print(i)

#from random import randint
#l=[randint(-100, 100) for x in range(10)]
#n=0
#for i in range(10):
#    if l[i]<0 and l[i+1]<0:
#        n=n+1
#print(l,n)














