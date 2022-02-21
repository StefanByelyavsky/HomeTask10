z = 'yes'
while z == 'yes' or z == 'y':
    a = input('задайте действие :')
    print(a)
    b = list(a)
    if b[-2] == "/" and b[-1] == '0':
        print('На ноль делить нельзя')
    else:
        c = eval(a)
        print(c)
    z = input('Желаете продолжить? (Yes\\No):').lower().strip()
    while z != 'yes' and z != 'no' and z != 'y' and z != 'n':
        print('введите корректный ответ')
        z = input('Желаете продолжить? (Yes\\No):').lower().strip()
print('END')
