import funk
place=[[0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0]]
k = int(input("Введите текущую координату фигуры(вертикаль): "))
k=k-1
l = int(input("Введите текущую координату фигуры(горизонталь): "))
l=l-1
m = int(input("Введите координату для хода(вертикаль): "))
m=m-1
n = int(input("Введите координату для хода(горизонталь): "))
n=n-1


place[l][k] = 1
place[n][m] = 1
funk.print_matrix(place)
funk.move_queen(place, k, l, m, n)



    