import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Определяем переменные
x, y = sp.symbols("x y")

# Определяем уравнения системы
eq1 = sp.tan(x * y) - x**2
eq2 = 0.8 * x**2 + 2 * y**2 - 1

# Создаем функции для уравнений для построения контура
f_eq1 = sp.lambdify((x, y), eq1, "numpy")
f_eq2 = sp.lambdify((x, y), eq2, "numpy")

# Создаем сетку для построения графика
x_vals = np.linspace(-2, 2, 400)
y_vals = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z1 = f_eq1(X, Y)
Z2 = f_eq2(X, Y)

# Строим контурный график
plt.figure()
plt.contour(X, Y, Z1, levels=[0], colors="r", label="eq1")
plt.contour(X, Y, Z2, levels=[0], colors="b", label="eq2")
plt.xlabel("x")
plt.ylabel("y")
plt.title("График системы уравнений")
plt.legend()
plt.grid(True)
plt.show()
