def f(x):
    return x ** 2 + x ** 0.5


def solve(c, a, b):
    eps = 1e-7
    l, r = a, b

    while r - l > eps:
        m = (l + r) / 2.0
        if f(m) < c:
            l = m
        else:
            r = m

    return l

if __name__ == '__main__':
    C = float(input())
    print(f"{solve(C, 0, C):.6f}")
