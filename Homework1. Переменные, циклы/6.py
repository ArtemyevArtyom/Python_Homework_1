"""
6) Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
a = int(input('Введите параметр a(км): '))
b = int(input('Введите параметр b(км): '))
day = 1
print(" %d %s %d %s" % (day, '-й день:', a, '(км)'))
while a < b:
    a *= 1.1
    day += 1
    print(" %d %s %.2f %s" % (day, '-й день:', a, '(км)'))
print("%s %d %s %d %s %.2f" % ('Результат спортсмена составит не менее', b, 'километров на', day, '-й день:', a))
