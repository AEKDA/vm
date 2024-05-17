import sympy as sp
import util


async def solve(f, channel):

    channel.put("Ввод интервала a и b через пробел: ")
    msg = await channel.get()
    a, b = map(float, msg.split(" "))

    channel.put("Ввод точности: ")
    msg = await channel.get()
    eps = float(msg)

    header = ["a", "b", "x", "f(a)", "f(b)", "f(x)", "abs(a -b)"]
    ans = []

    x_symbol = sp.Symbol("x")

    while True:
        x = (a + b) / 2

        val_x = f.subs(x_symbol, x)
        val_a = f.subs(x_symbol, a)

        if val_a * val_x > 0:
            a = x
        else:
            b = x

        ans.append([a, b, x, val_a, f.subs(x_symbol, b), val_x, abs(a - b)])

        if abs(val_x) < eps:
            util.print_table(ans, headers=header)
            break
    return x
