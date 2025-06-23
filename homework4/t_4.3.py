#Знайдіть найменше 𝑥∈[0, 10], що 𝑓(𝑥) = 𝑥³ + 𝑥 + 1 > 5. - функція монотонно зростаюча

def f(x):
    return x ** 3 + x + 1


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


print(f"Root = {solve(5, 0, 10):.6f}")