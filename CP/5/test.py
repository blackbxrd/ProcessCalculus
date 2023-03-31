n = int(input("Введите натуральное число n: "))
a = []
for i in range(n):
    a.append(float(input(f"Введите действительное число a{i+1}: ")))
sum_a = sum(a)
result = 2 * sum_a ** 2
print(f"Результат вычисления выражения 2(a1+..+..+..+an)^2 равен {result}")