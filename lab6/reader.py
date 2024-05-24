def DE(funcs):
    in_str = [f"{i}. {val['str']}" for (i, val) in enumerate(funcs)]
    print(*in_str, sep="\n")
    return funcs[int(input("Ввод: ").strip())]
