import sympy as sp
import numpy as np
import util


def solve(f, a, b, eps, n):

    header = ["xi", "xi+1", "phi(xi+1)", "f(xi+1)", "abs(xi-1 - xi)"]
    ans = []

    x_symbol = sp.Symbol("x")
    df = sp.diff(f, x_symbol)
    df_a, df_b = df.subs(x_symbol, a), df.subs(x_symbol, b)

    lam = -1 / abs(max(abs(df_a), abs(df_b))) * (df_a / abs(df_a))
    x = a

    x_val = x
    df_lambda = sp.lambdify(x_symbol, df)

    print(abs(df_lambda(a)), abs(df_lambda(b)))

    for i in np.arange(a, b, 0.1):
        if abs(df_lambda(i)) >= 1:
            print("Достаточное условие сходимости не выполняется")
            break

    while True:
        new = x + lam * f.subs(x_symbol, x)
        ans.append(
            [x, new, x + lam * f.subs(x_symbol, x), f.subs(x_symbol, new), abs(new - x)]
        )
        if abs(f.subs(x_symbol, new)) < eps:
            util.print_table(ans, headers=header)
            return x
        x = new
        n-=1
        if n <0:
            return x
