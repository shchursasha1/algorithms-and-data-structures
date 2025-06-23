def f(n):                     # O(n)
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum

#optimized function:
def new_f(n):                # O(1)
    return n * (n + 1) // 2


def g(n):
    sum = 0                   # O(1)
    for i in range(1, n + 1): # O(n)
        sum = sum + i + f(i)  # (O(1) + O(2) + O(3) + ... + O(n))
    return sum                # O(1)

#res: (O(1) + O(2) + O(3) + ... + O(n))

#Перепишемо за означенням:
# (C + 2 C + 3 C + ... + n C) =
# = C(n * (n + 1) // 2) =
# = C * (n^2 + n) // 2 = O(n^2)

# Цю функцію можна покращіти, якщо ми використаємо покращену функцію f(а саме функцію new_f).
# В результаті функція g буде мати асимптотичну оцінку O(n)