#вывод в консоль

print(5)
print(5, 7, 9)

n = 5
print(n)

n1 = None
print(n1)

n2 = 1.89
print(n2)

# строки

n3 = 'fddf'
print(n3)
n4 = "srgeqg"
print(n4)

# вывод типа данных

n5 = 5
print(type(n5))

n6 = 'sdds'
print(type(n6))

# вывод ковычек

n7 = 'fds\'fds'
print(n7)

n8 = 'fds"fdjk"fds'
print(n8)

# способы закомментить

# решетка для одной строки или
"""
три опострофа или кавычки в начале и конце
для многострочного комментария
"""

# интерполяция

a = 5
b = 5.54
c = 'hello'

print (a, '-', b, '-', c)

print(f"{a} - {b} - {c}")  # f стороки

print("{} - {} - {}".format(a,b,c))

# ввод данных (по умолчанию принимают тип данных str)

print('Введите первое число: ')
d = input()
print (d)
e = input('Введите второе число: ')

# функция сложения двух чисел

print(d, '+', e, '=', d+e)

# приведение типов

f = 5.89
print (f)
print (type(f))

# если мы хотим привести это число к целочисельному типу даных, то используем функцию int

f = int(f)
print (f)
print (type(f))

g = 1
print (g)
print (type(g))

# приведем к типу данных bool

g = bool(g)
print (g)
print (type(g))

# исправление сложения 

ab = int(input('Введите первое число: '))
ba = int(input('Введите второе число: '))
print(ab, '+', ba, '=', ab+ba)




# функция округления чисел - round

a = 5.76439
b = 6.342232
print(round(a*b, 3))

# сокращенное присваивание

iter = 2
iter += 3
iter /= 3

# вывод значений из строки

a = 'qwerty'
print (a[0])

for i in a:
    print (i)


# оператор for

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)

# функции

text = 'СъЕШЬ ещё этих МяГкИх французскиз булок'
print(len(text)) #длина
print('ещё' in text) #проверка наличия
print(text.lower()) #переводит все в нижний регистр
print(text.upper()) #переводит все в верзний регистр
print(text.replace('ещё', 'ЕЩЁ')) #замена


