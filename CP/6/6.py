n = int(input("Введите количество чисел в последовательности: "))
a = []
for i in range(n):
    a.append(int(input(f"Введите число a{i+1}: ")))

count = 0
for num in a:
    if num % 2 != 0:
        count += 1

print(f"Количество нечетных чисел в последовательности: {count}")