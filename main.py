"""""
В России применяются регистрационные знаки нескольких видов. Общего в них то, что они состоят из цифр и букв. Причём используются только
12 букв кириллицы, имеющие графические аналоги в латинском алфавите — А, В, Е, К, М, Н, О, Р, С, Т, У и Х.
У частных легковых автомобилях номера — это буква, три цифры, две буквы, затем две или три цифры с кодом региона. У такси — две буквы, три цифры,
затем две или три цифры с кодом региона. Есть также и другие виды, но в этой задаче они не понадобятся.
Вам потребуется определить, является ли последовательность букв корректным номером указанных двух типов, и если является, то каким.
На вход даются строки, которые претендуют на то, чтобы быть номером. Определите тип номера. Буквы в номерах — заглавные русские. Маленькие 
и английские для простоты можно игнорировать.
"""""
import re
b='А777АА777'
print(re.findall(r[АВЕКМНОРСТУХ]\d\d\d[АВЕКМНОРСТУХ]{2}\d{2,3},b),'номер машины')
print(re.findall(r[АВЕКМНОРСТУХ]\d\d\d[АВЕКМНОРСТУХ]{2}\d{2,3},b),'номер такси')
















