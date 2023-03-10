n=int(input("Введите n: "))
k=0
for i in range(1,n+1):
    print("a",i,' =',end='')
    a=int(input())
    if (a%2!=0):
        k+=1
print('Столько элементов нечётные ->',k)