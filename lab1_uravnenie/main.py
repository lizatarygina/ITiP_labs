a = float(input('Введите коэффицент a '))
b = float(input('Введите коэффицент b '))
c = float(input('Введите коэффицент c '))

d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b + d**0.5)/(2*a)
    x2 = (-b - d**0.5)/(2*a)
    print('Корни уравнения: ', x1, ' и ', x2)
elif d == 0:
    x1 = -b/2*a
    print('Корень уравнения: ', x1)
else:
    print('У уравнения нет корней')

