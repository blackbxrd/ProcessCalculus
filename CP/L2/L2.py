import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

####################################################################################################
###################### создать случайную матрицу numpy array #######################################
####################################################################################################

# Задаём размеры матрицы (5 строк, 3 столбца)
rows = 5
cols = 3

# Создаём матрицу размера rows x cols с случайными значениями от 0 до 1
matrix = np.random.randint(-10, 10, (rows, cols))

# Вывод матрицу на экран
print(matrix)




####################################################################################################
##################### построить тепловую карту на основе созданной матрицы  ########################
####################################################################################################


# Строим тепловую карту на основе матрицы
plt.imshow(matrix, cmap='hot', interpolation='nearest')
plt.colorbar()

# Показать тепловую карту
plt.show()


####################################################################################################
#################### превраить матрицу в массив, построить гистограмму (seaborn) ###################
####################################################################################################

# Превращаем матрицу в массив
array = matrix.flatten()

# Строим гистограмму на основе массива
sns.histplot(array)

# Показать гистограмму
plt.show()


