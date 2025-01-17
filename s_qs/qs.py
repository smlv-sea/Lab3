import matplotlib.pyplot as plt
import numpy as np

# Цикл по всем файлам
for i in range(65):
    # Чтение данных из файла
    data = np.loadtxt(f'iteration_{i}.txt')

    # Создание изображения
    plt.figure(figsize=(8, 6))
    plt.plot(data)
    plt.title(f'Step {i}')
    plt.savefig(f'step_{i}.png')
    plt.close()
