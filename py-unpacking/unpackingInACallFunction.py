def fun(a, b, c, d, *rest):
    print(a, b, c, d, rest)


fun(*[1, 2], 3, *range(4, 7))