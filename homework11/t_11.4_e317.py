import sys

sys.set_int_max_str_digits(400000)

def solve(X, Y):
    if len(X) == 0 or len(Y) == 0:
        return 0
    if len(X) <= 3 and len(Y) <= 3:
        return int(X) * int(Y)

    n = max(len(X), len(Y))
    m = n // 2

    X = X.zfill(n)
    Y = Y.zfill(n)

    a, b = X[:-m], X[-m:]
    c, d = Y[:-m], Y[-m:]

    p1 = solve(a, c)
    p2 = solve(b, d)
    p3 = solve(str(int(a) + int(b)), str(int(c) + int(d)))

    return (10 ** (2 * m)) * p1 + (10 ** m) * (p3 - p1 - p2) + p2


if __name__ == "__main__":
    X, Y = map(str, input().split())
    print(solve(X, Y))