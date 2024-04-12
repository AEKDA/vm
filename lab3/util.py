from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


def print_table(data, headers=None):
    if headers is not None:
        print(tabulate(data, headers=headers, showindex=True))
    else:
        print(tabulate(data))


def print_chart(f, a, b):
    x_values = np.linspace(a, b, 100)

    y_values = [f(x) for x in x_values]

    # Строим график
    plt.plot(x_values, y_values)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("График функции f(x)")
    plt.grid(True)
    plt.show()


def exact_integral(func, a, b):
    sym_x = sp.symbols("x")

    f = sp.sympify(func)

    indefinite_integral = sp.integrate(f, sym_x)
    exact_value = indefinite_integral.subs(sym_x, b) - indefinite_integral.subs(
        sym_x, a
    )
    return exact_value, exact_value.evalf()
