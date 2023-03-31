import numpy as np
import torch
import time

# Размеры матриц
n = 10
m = 10
k = 10

# Инициализируем матрицы случайными значениями
A = np.random.rand(n, m)
B = np.random.rand(m, k)
A_torch = torch.from_numpy(A).float()
B_torch = torch.from_numpy(B).float()

# Перемножение матриц как списки Python
start_time = time.time()
C_list = [[sum(a * b for a, b in zip(row_A, col_B)) for col_B in zip(*B)] for row_A in A]
end_time = time.time()
print(f"Время перемножения матриц как списки Python: {end_time - start_time:.4f} секунд")

# Перемножение матриц как NumPy массивы
start_time = time.time()
C_numpy = np.dot(A, B)
end_time = time.time()
print(f"Время перемножения матриц как NumPy массивы: {end_time - start_time:.4f} секунд")

# Перемножение матриц на CPU с помощью PyTorch
start_time = time.time()
C_torch_cpu = torch.mm(A_torch, B_torch)
end_time = time.time()
print(f"Время перемножения матриц на CPU в помощью PyTorch: {end_time - start_time:.4f} секунд")

# Перемножение матриц на GPU с помощью PyTorch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
A_torch = A_torch.to(device)
B_torch = B_torch.to(device)
start_time = time.time()
C_torch_gpu = torch.mm(A_torch, B_torch)
torch.cuda.synchronize()
end_time = time.time()
print(f"Время перемножения матриц на GPU в помощью PyTorch: {end_time - start_time:.4f} секунд")

# Проверяем корректность перемножения
assert np.allclose(C_list, C_numpy)
assert torch.allclose(C_numpy, C_torch_cpu)
assert torch.allclose(C_numpy, C_torch_gpu.cpu())