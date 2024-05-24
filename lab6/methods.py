def euler(f, a, b, y0, h):
    dots = [(a, y0)]
    n = int((b - a) / h)

    for i in range(1, n + 1):
        x, y = dots[i - 1][0], dots[i - 1][1]
        dots.append((x + h, y + h * f(x, y)))

    return dots


def upgraded_euler(f, a, b, y0, h):
    dots = [(a, y0)]
    n = int((b - a) / h)

    for i in range(1, n + 1):
        x, y = dots[i - 1][0], dots[i - 1][1]
        dots.append((x + h, y + h / 2 * (f(x, y) + f(x + h, y + h * f(x, y)))))

    return dots


def adams(f, a, b, y0, h):
    n = int((b - a) / h)
    # b0 = min(b, a + 3 * h)
    # dots = euler(f, a, b0, y0, h)
    dots = euler(f, a, b, y0, h)
    while len(dots) < 4:
        h /= 2
        dots = euler(f, a, b, y0, h)
    dots = dots[:4]

    for i in range(4, n + 1):

        df = f(dots[i - 1][0], dots[i - 1][1]) - f(dots[i - 2][0], dots[i - 2][1])
        d2f = (
            f(dots[i - 1][0], dots[i - 1][1])
            - 2 * f(dots[i - 2][0], dots[i - 2][1])
            + f(dots[i - 3][0], dots[i - 3][1])
        )
        d3f = (
            f(dots[i - 1][0], dots[i - 1][1])
            - 3 * f(dots[i - 2][0], dots[i - 2][1])
            + 3 * f(dots[i - 3][0], dots[i - 3][1])
            - f(dots[i - 4][0], dots[i - 4][1])
        )
        dots.append(
            (
                dots[i - 1][0] + h,
                dots[i - 1][1]
                + h * f(dots[i - 1][0], dots[i - 1][1])
                + (h**2) * df / 2
                + 5 * (h**3) * d2f / 12
                + 3 * (h**4) * d3f / 8,
            )
        )

    return dots
