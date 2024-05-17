from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


def print_table(data, headers=None):
    if headers is not None:
        print(tabulate(data, headers=headers, showindex=True))
    else:
        print(tabulate(data))


def make_graphics(funcs):
    # Определяем переменные
    x, y = sp.symbols("x y")
    # Создаем функции для уравнений для построения контура
    f_eq1 = sp.lambdify((x, y), funcs[0], "numpy")
    f_eq2 = sp.lambdify((x, y), funcs[1], "numpy")

    # Создаем сетку для построения графика
    x_vals = np.linspace(-10, 10, 400)
    y_vals = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z1 = f_eq1(X, Y)
    Z2 = f_eq2(X, Y)

    # Строим контурный график
    plt.figure()
    plt.contour(X, Y, Z1, levels=[0], colors="r")
    plt.contour(X, Y, Z2, levels=[0], colors="b")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Plot of functions")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(color="gray", linestyle="--", linewidth=0.5)
    plt.legend(["eq1", "eq2"])
    plt.show()


def make_graphic(func):

    # Создаем символьные переменные
    x, y = sp.symbols("x y")

    # Plot the functions
    plt.figure(figsize=(8, 6))

    # Решаем уравнение относительно y
    try:
        y_values = sp.solve(func, y)
        if not y_values:
            y_values = sp.solve(func - y, y)
            if not y_values:
                raise ValueError("sympy cannot do this")
    except Exception as e:
        raise ValueError("sympy cannot do this")
    for i, y_val in enumerate(y_values):
        f = sp.lambdify(x, y_val, modules=["numpy"])
        # Генерируем значения x для построения графика
        x_values = np.linspace(-10, 10, 400)
        # Генерируем значения y для текущей функции
        y_values_i = f(x_values)
        # Plot the function
        plt.plot(x_values, y_values_i, label=f"y{i+1} of {func}")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Plot of functions")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(color="gray", linestyle="--", linewidth=0.5)
    plt.legend()
    plt.show()
