#1

var1 = 6
var2 = int(input('Введите число: '))
var3 = (var1 + var2)**int(input('Введите степень: '))
print(var3)

print(f'Some string {input("Input string, please: ")}')

#2

time_sec = int(input('Введите время в секундах: '))
time_hour = time_sec // 3600
time_min = (time_sec % 3600) // 60
time_sec_fin = (time_sec % 3600) % 60

if len(str(time_hour)) < 2:
    time_hour = f'0{time_hour}'

if len(str(time_min)) < 2:
    time_min = f'0{time_min}'

if len(str(time_sec_fin)) < 2:
    time_sec_fin = f'0{time_sec_fin}'

print(f'Время: {time_hour}.{time_min}.{time_sec_fin}')


#3

num = int(input('Введите число от 0 до 9: '))

print(num*100 + 20*num + 3*num)


#4

num = int(input('Введите число: '))

max = 0

while num:
    iter = num % 10
    if iter > max:
        max = iter
    num //= 10

print(max)

#5

proceeds = int(input('Введите выручку: '))
loss = int(input('Введите издержки: '))

if proceeds > loss:
    print('Фирма не убыточна')
    print('Рентабельность: {}'.format((proceeds - loss)/proceeds))
    print(f'Прибыль в расчете на одного сотрудника: {(proceeds-loss)/int(input("Введите число сотрудников: "))}')
elif proceeds < loss:
    print('Фирма убыточна')
else:
    print('Фирма на грани')

#6

def func(a, b):
    i = 0
    while a < b:
        i += 1
        a += a*0.1
        print(f'День {i}: {a}')
    else:
        print('Норматив сделан!')
    return i

res = func(int(input('Введите a: ')),int(input('Введите b: ')))

print(res)



