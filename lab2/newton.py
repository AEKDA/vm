import sympy as sp
import util


def solve(f, a: int, b: int, eps: int):

    header = ["xk", "f(xk)", "f'(xk)", "xk+1", "abs(xk+1 - xk)"]
    ans = []

    x_symbol = sp.Symbol("x")

    df = sp.diff(f, x_symbol)
    ddf = sp.diff(df, x_symbol)

    if ddf.subs(x_symbol, a) * f.subs(x_symbol, a) > 0:
        x = a
    else:
        x = b

    while True:
        val_x = f.subs(x_symbol, x)
        dval_x = df.subs(x_symbol, x)
        new = x - val_x / dval_x

        ans.append([x, val_x, dval_x, new, abs(new - x)])
        x = new
        if abs(val_x) < eps and abs(new - x) < eps:
            util.print_table(ans, headers=header)
            break
    return x
