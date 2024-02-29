from tabulate import tabulate


def print_table(data, headers=None):
    if headers is not None:
        print(tabulate(data, headers=headers, showindex=True))
    else:
        print(tabulate(data))
