

def check_first_move(place):#проверка на первый ход
    i = 0
    j = 0
    choice = 0
    for  i in range(1,8):
    
        for j in range(1,8):
        
            if (place[i][j] == 1):
                choice=+1
        
    
    if (choice == 0):
    
        print(" - Да, это возможно сделать за 1 ход!")
    
    else:
    
        print(" - Нет, это не возможно за один ход!")
        
    
    
def move_queen (place,  k,  l,  m,  n):
    
    for i in range(0, 8):
    
        place[l][i] = 7
        place[i][k] = 7
        if (((l + i) <= 8) and ((k + i) <= 8)):
            place[l + i][k + i] = 7
        if (((l + i) <= 8) and ((k - i) > 0)):
            place[l + i][k - i] = 7
        if (((l - i) > 0) and ((k + i) <= 8)):
            place[l - i][k + i] = 7
        if (((l - i) > 0) and ((k - i) > 0)):
            place[l - i][k - i] = 7
        
    
    print ("Возможно ли КОРОЛЕВОЙ попасть c поля (", k + 1, ";", l + 1, ") на поле (", m + 1, ";", n + 1, ") ? ")
    check_first_move(place)
    

    
#"Что бы за 2-а хода, добраться до поля (" , m + 1 , ";" , n + 1 , "), в 1-ый ход нужно переместиться на поле (" , k + 1 , ";" , n + 1 , ")"

    
def print_matrix(place):
    for arr in place:
        print(arr)




        

        