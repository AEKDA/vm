import util


def f(x: float) -> float:
    return -2 * x**3 - 4 * x**2 + 8 * x - 4


def trapeze(f, a: float, b: float, n) -> float:
    h = (b - a) / n
    return h * ((f(a) + f(b)) / 2 + sum([f(a + i * h) for i in range(1, int(n))]))


def middle(f, a: float, b: float, n) -> float:
    h = (b - a) / n
    return h * sum([f((a + i * h) - h * 1 / 2) for i in range(1, int(n) + 1)])


def left(f, a: float, b: float, n) -> float:
    h = (b - a) / n
    return h * sum([f(a + i * h) for i in range(1, int(n) + 1)])


def right(f, a: float, b: float, n) -> float:
    h = (b - a) / n
    return h * sum([f(a + (i - 1) * h) for i in range(1, int(n) + 1)])


def simpson(f, a: float, b: float, n) -> float:
    h = (b - a) / n
    return (
        h
        / 3
        * (
            f(a)
            + 4 * sum([f(a + i * h) for i in range(1, int(n), 2)])
            + 2 * sum([f(a + i * h) for i in range(2, int(n) - 1, 2)])
            + f(b)
        )
    )


def calc(method, a, b, n, eps):
    header = ["value"]
    ans = []

    k = method["k"]
    start = method["f"](f, a, b, n)

    ans.append([start])

    while True:
        n *= 2
        val = method["f"](f, a, b, n)
        if abs(val - start) / (2**k - 1) < eps:
            util.print_table(data=ans, headers=header)
            return val, n
        start = val
        ans.append([start])


methods = [
    {"name": "Левых прямоугольников", "k": 1, "f": left},
    {"name": "Правых прямоугольников", "k": 1, "f": right},
    {"name": "Средних прямоугольников", "k": 2, "f": middle},
    {"name": "Трапеции", "k": 2, "f": trapeze},
    {"name": "Симпсона", "k": 4, "f": simpson},
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

    a, b = 1, 2
    n = 5
    eps = 0.0001

    ans = calc(method, a, b, n, eps)

    print(
        "Значение интеграла и число разбиений:",
        abs(ans[0]),
        ans[1],
        "границы:",
        a,
        b,
    )
