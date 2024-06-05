import util
import internal
import sympy as sp


def f1(x):
    return -2 * x**3 - 4 * x**2 + 8 * x - 4


def f2(x):
    return -(x**3) - x**2 + 2 * x + 1


def f3(x):
    return 2 * x**3 - 2 * x**2 + 7 * x - 14


methods = [
    {"name": "Левых прямоугольников", "k": 1, "f": internal.left},
    {"name": "Правых прямоугольников", "k": 1, "f": internal.right},
    {"name": "Средних прямоугольников", "k": 2, "f": internal.middle},
    {"name": "Трапеции", "k": 2, "f": internal.trapeze},
    {"name": "Симпсона", "k": 4, "f": internal.simpson},
]
funcs = [
    {"name": "-2 * x**3 - 4 * x**2 + 8 * x - 4", "f": f1},
    {"name": "-(x**3) - x**2 + 2 * x + 1", "f": f2},
    {"name": "2 * x**3 - 2 * x**2 + 7 * x - 14", "f": f3},
]

if __name__ == "__main__":

    in_str = "\n".join(
        [str(i) + ". " + name["name"] for (i, name) in enumerate(methods)]
    )

    try:
        method = methods[
            int(input(f"Выберите метод из предложенных\n{in_str}\nВвод: "))
        ]
    except:
        exit("Не правильный выбор метода")

    in_str = "\n".join([str(i) + ". " + name["name"] for (i, name) in enumerate(funcs)])
    try:
        func = funcs[int(input(f"Выберите функцию из предложенных\n{in_str}\nВвод: "))]
    except:
        exit("Не правильный выбор функции")

    a, b = map(int, input("Введите промежуток a и b через пробел: ").split(" "))

    # util.print_chart(func["f"], a - 5, b + 5)

    n = 10
    eps = 0.01
    # eps = float(input("Введите eps: "))

    ans = internal.calc(func["f"], method, a, b, n, eps)

    print(
        "Значение интеграла и число разбиений:",
        ans[0],
        ans[1],
        "границы:",
        a,
        b,
    )

    print("реальное значение интеграла: ", util.exact_integral(func["name"], a, b))
