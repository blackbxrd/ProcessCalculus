import random

#Даны натуральное число n, действительные числа a1,..., an. Вычислить:2(a1+..+..+..+an)^2


def zapolni_list(list):

    n = int(input('Введите кол-во элементов списка: '))
    list=[] 
    for i in range(n):
        list.append(float(input(f"Введите действительное число a{i+1}: ")))
        
        
        
    return list

def rand_list(list):
    n = int(input('Введите кол-во элементов списка: '))
    list=[] 
    for i in range(n):
        
         list.append(random.randint(0, 100))
    print(list)
        
    return list

def func_sum(list):
    
    sum=0
    for i in range(len(list)):
        
        sum+=list[i]
        
    return sum
        
list=[]
chek=int(input('1-заполнить самому\n2-автозаполнение'))
if chek==1:
   list2=zapolni_list(list)
elif chek==2:
   list2=rand_list(list)
else:
    
    raise Exception('Ошибка') 
sum_a = sum(list2)
result = 2 * sum_a ** 2
print(f'res = {result}')





#2*(sum(a))**2
