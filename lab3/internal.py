import util
import sympy as sp


x_s = sp.symbols("x")


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


def calc(func, method, a, b, n, eps):
    header = ["value"]
    ans = []

    k = method["k"]
    start = method["f"](func, a, b, n)

    ans.append([start])

    while True:
        n *= 2
        val = method["f"](func, a, b, n)
        if abs(val - start) / (2**k - 1) < eps:
            util.print_table(data=ans, headers=header)
            return val, n
        start = val
        ans.append([start])
