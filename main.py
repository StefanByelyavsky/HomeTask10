z = 'yes'
while z == 'yes' or z == 'y':
    a = input('задайте действие :')
    print(a)
    b = list(a)
    if b[-1] != 0 and b[-2] != '/':
        a = eval(a)
        print(a)
    else:
        print('На ноль делить нельзя')
    z = input('Желаете продолжить? (Yes\\No):').lower().strip()
    while z != 'yes' and z != 'no' and z != 'y' and z != 'n':
        print('введите корректный ответ')
        z = input('Желаете продолжить? (Yes\\No):').lower().strip()
print('END')
