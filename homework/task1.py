#1
a=3
b=6
c=7
print(a+b+c/3)
#2
a = 2
b = 4
c = 7
if a < b and a < c:
    print(a)
    if b > c:
        print(b)
    else:
        print(c)
e = [2, 5, 4, 8]
print(e)
print(type(e))
#3
y = 2020
if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
    print("обычный")
else:
    print("високосный")
#4
x = 3
y = 4
z = 5
if (x + y) > z and (x + z) > y and(z + y) > x :
    print("yes")
else:
    print("no")
print("решаем уравнение a * x ** 2 + b * x + c = 0")
#5
a = int(input(-1))
b = int(input(-2))
c = int(input(15))
discriminant = b ** 2 - 4 * a * c
print("Дискриминант = " + str(discriminant))
if discriminant < 0:
    print("Корней нет")
elif discriminant == 0:
    x = -b / (2 * a)
    print("x = " + str(x))
else:
    x1 = (-b - discriminant ** 0.5) / (2 * a)
    x2 = (-b + discriminant ** 0.5) / (2 * a)
    print(" x1 = " + str(x1))
    print(" x2 = " + str(x2))
#6
x = 3
y = 5
r = 7
if x < r or y < r:
    print("yes")
else:
    print("no")