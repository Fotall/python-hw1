# про шоколадку
# 3 2 4 -> yes
# 3 2 1 -> no
print('Введите размеры шоколадки ')
chocolateN = int(input('по горизонтали:  '))
chocolateM = int(input('по вертикали:  '))
deliteCocolate = int(input('сколько долек надо отломать(от 1 до 4):  '))
if (deliteCocolate == 2):
    if (chocolateN == 2 and chocolateM > 1): 
        print('yes')
    elif (chocolateN == 1 and chocolateM % 2 == 0):
        print('yes')
    else:
        print('no')
elif (deliteCocolate == 3):
    if (chocolateN == 1 and chocolateM % 2 == 0):
        print('yes')
    else:
        print('no')
elif (deliteCocolate == 4):
    if (chocolateN == 2 and chocolateM > 1): 
        print('yes')
    elif  (chocolateN == 1 and chocolateM % 4 == 0): 
        print('yes')
    else:
        print('no')
elif (deliteCocolate == 1):
    if (chocolateN == 1):
        print('yes')
    else:
        print('no')
else:
    print('программа пока написана для вычесления от 1 до 4')


