import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


def make_grafic(x, y, approximate_function, point, isBlock: bool = True):
    fig, ax = plt.subplots()
    xnew = np.linspace(np.min(x), np.max(x), 100)
    ynew = [approximate_function(x, y, i) for i in xnew]
    plt.plot(x, y, "o", label="Входные точки")
    plt.plot(xnew, ynew, label="Функция аппр.")
    plt.plot(point[0], point[1], ".", markersize=12, label="Аппроксимация")
    plt.title(approximate_function.__name__)
    ax.legend()
    plt.grid(True)
    plt.show(block=isBlock)


def print_table(data, headers=None):
    if headers is not None:
        print(tabulate(data, headers=headers, showindex=True))
    else:
        print(tabulate(data))
