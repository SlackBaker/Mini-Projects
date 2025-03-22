import math
import matplotlib.pyplot as plt
import numpy as np  # Додаємо імпорт для numpy

def solve_quadratic(a, b, c):
    D = (b ** 2) - (4 * a * c)
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("x1 = ", x1, " x2 = ", x2)
    else:
        print("error")

def viet_quadratic(x1, x2):
    p = -1 * (x1 + x2)
    q = x1 * x2
    return p, q

def plot_function(func, x_range):
    # Створюємо масив значень x
    x = np.linspace(x_range[0], x_range[1], 1000)

    # Обчислюємо відповідні значення функції
    y = func(x)

    # Створюємо графік
    plt.plot(x, y)

    # Додаємо заголовок та підписи осей
    plt.title("Графік функції")
    plt.xlabel("x")
    plt.ylabel("y")

    # Показуємо графік
    plt.grid(True)
    plt.show()

# Приклад використання
def my_function(x):
    return x  # Виправлено: np.sin замість plt.sin

# Малюємо графік функції від -10 до 10
plot_function(my_function, (-10, 10))
