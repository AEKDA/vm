import matplotlib.pyplot as plt


def plot(real, euler, upgraded_euler, adams):
    plt.figure(figsize=(12, 8))

    real_x, real_y = [x[0] for x in adams], real
    plt.plot(real_x, real_y, label="True Values", linewidth=3, marker="d", markersize=2)

    euler_x, euler_y = list(map(lambda x: x[0], euler)), list(
        map(lambda x: x[1], euler)
    )

    plt.plot(
        euler_x, euler_y, label="Euler's Method", linewidth=1, marker="o", markersize=2
    )

    upgraded_euler_x, upgraded_euler_y = list(
        map(lambda x: x[0], upgraded_euler)
    ), list(map(lambda x: x[1], upgraded_euler))
    plt.plot(
        upgraded_euler_x,
        upgraded_euler_y,
        label="Upgraded euler's Method",
        linewidth=1,
        marker="x",
    )

    adams_x, adams_y = list(map(lambda x: x[0], adams)), list(
        map(lambda x: x[1], adams)
    )

    plt.plot(adams_x, adams_y, label="Adams Method", linewidth=1, marker="s")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Comparison of Different Methods")
    plt.legend()
    plt.grid(True)

    plt.show()
