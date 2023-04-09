# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
a = int(input('Введите трехзначное число:'))
if (99 < a < 1000):
    s = str(a)
    b = int(s[0]) + int(s[1]) + int(s[2])
    print(b)
else:
     print('трехзначное!!!')


#6 -> 1  4  1
#24 -> 4  16  4
#    60 -> 10  40  10

nunber = int(input('Введите кол-во журавликов, кратное 6:'))
petr = int(nunber / 6)
serg = petr
kate = 4 * petr
print('Катя наштамповала:', kate, 'Петя:', petr, 'Сережа:', serg)


# 385916 -> yes
# 123456 -> no
tiscet = int(input('Введите ваш билет:'))
s = str(tiscet)
firstSum = int(s[0]) + int(s[1]) + int(s[2])
secondSum = int(s[3]) + int(s[4]) + int(s[5])
if (firstSum == secondSum):
    print('you win!')
else:
    print('you lose')

