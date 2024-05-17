import sympy as sp
import util


def solve(funcs_start, funcs, init_approx, eps, n):

    header = ["x", "y", "f(x,y)", "abs(xk+1 - xk)"]
    ans = []

    x_symbol = sp.Symbol("x")
    y_symbol = sp.Symbol("y")

    for func in funcs:

        df1 = sp.diff(func, x_symbol)
        df2 = sp.diff(func, y_symbol)
        if (
            abs(df1.subs({x_symbol: init_approx[0], y_symbol: init_approx[0]}))
            + abs(df2.subs({x_symbol: init_approx[0], y_symbol: init_approx[0]}))
            > 1
        ):
            print(
                "Достаточное Условие сходимости не выполняется",
                abs(df1.subs({x_symbol: init_approx[0], y_symbol: init_approx[0]}))
                + abs(df2.subs({x_symbol: init_approx[0], y_symbol: init_approx[0]})),
            )
            break

    while True:
        tmp = []
        for func in funcs:
            v = func.subs({x_symbol: init_approx[0], y_symbol: init_approx[1]})
            tmp.append(v.evalf())

        f_x = funcs_start[0].subs({x_symbol: tmp[0], y_symbol: tmp[1]})
        f_y = funcs_start[1].subs({x_symbol: tmp[0], y_symbol: tmp[1]})

        ans.append(
            [
                init_approx[0],
                init_approx[1],
                [f_x, f_y],
                [abs(tmp[0] - init_approx[0]), abs(tmp[1] - init_approx[1])],
            ]
        )
        if abs(f_x) < eps and abs(f_y) < eps:
            util.print_table(ans, headers=header)
            return tmp

        init_approx = tmp
        n -= 1
        if n < 0:
            print("Остновились на значениях")
            return tmp
