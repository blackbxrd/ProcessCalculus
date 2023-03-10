import random

#Даны натуральное число n, действительные числа a1,..., an. Вычислить:2(a1+..+..+..+an)^2


def zapolni_list(list):

    n = int(input('Введите кол-во элементов списка: '))
    list=[0] * n
    for i in range(0,n+1):
        
        list[i]=int(input((f'Введите значение a{i}=')))
        
    return list

def rand_list(list):
    n = int(input('Введите кол-во элементов списка: '))
    list=[0] * n
    for i in range(0,n+1):
        
        list[i]=random.randint(0, 100)
        
    return list

def func_sum(list):
    
    sum=0
    for i in range(1,len(list)):
        
        sum+=list[i]
        
    return sum
        

chek=int(input('1-заполнить самому\n 2-автозаполнение'))
if chek==1:
    print(zapolni_list(list))
elif chek==2:
    print(rand_list(list))
else:
    
    raise Exception('Ошибка') 
print(f'res = {2*func_sum(list)**2}')





#2*(sum(a))**2
