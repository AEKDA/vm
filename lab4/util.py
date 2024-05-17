import numpy as np
import matplotlib.pyplot as plt


def make_grafic(func, name, func_str, x_arr, y_arr):
    x = np.linspace(-2, 20, 400)
    integer_x = np.arange(-2, 20, 2)
    y = func(x)
    # Добавление точек на график
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=func_str, color="blue")
    plt.axhline(y=0, color="r", linestyle="--")
    plt.scatter(x_arr, y_arr, color="red", label="points")
    plt.title(name)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.xticks(integer_x)
    plt.savefig("grafic1.jpg")
    plt.show()
