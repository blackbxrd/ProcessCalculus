import funk


k=int(input('Введите k '))
l=int(input('Введите l '))
m=int(input('Введите m '))
n=int(input('Введите n '))

if funk.queen_attack(k, l, m, n):
    print(f"Ферзь угрожает полю ({m, n})")
else:
    print(f"Ферзь не угрожает полю ({m, n})")




    
