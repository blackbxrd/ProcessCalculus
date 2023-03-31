import numpy as np
import matplotlib.pyplot as plt


# построить график любой сложной функции. 
# построить график этой же функции с добавлением шума (numpy, matplotlib);
# не забудьте подписи к подписи к осям, заголовок графика, легенду, координатную сетку


def f(x):
    return np.sin(x) + np.cos(2*x) + 0.5*x

#  массив x значений от 0 до 10 с шагом 0.1
x = np.arange(0, 10, 0.1)

#  массив y значений функции f(x)
y = f(x)

#  график функции f(x)
plt.plot(x, y, label="Исходная функция")

#  шум к массиву y
noise = np.random.normal(0, 0.5, len(y))
y_noisy = y + noise

#  график функции f(x) с добавлением шума
plt.plot(x, y_noisy,  label="Шумная функция")

#  подписи к осям, заголовок графика, легенду и координатную сетку
plt.xlabel("Значения x")
plt.ylabel("Значения y")
plt.title("График функции с добавлением шума")
plt.legend()
plt.grid(True)

# Показать график
plt.show()