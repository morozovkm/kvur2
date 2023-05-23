from math import sqrt
print('Решим квадратное уравнение!!!')
baddata = True
while baddata:
    try:
        a = int(input('Введите a: '))
        b = int(input('Введите b: '))
        c = int(input('Введите c: '))
        baddata = False
    except ValueError:
        print('Не удалось получить данные!!!')

D = (b * b) - (4 * a * c)

if D > 0:
    d = sqrt(D)
    X1 = ((-b) + d) / (2 * a)
    X2 = ((-b) - d) / (2 * a)
    print(f'Уравнение имеет два корня X1 = {X1}, X2 = {X2}.')

elif D == 0:
    X1 = (-b) / (2 * a)
    print(f'Уравнение имеет один корень X1 = {X1}.')
else:
    print('Уравнение не имеет корней')
