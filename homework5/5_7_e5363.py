import sys

def solve():
    try:
        n_line = sys.stdin.readline()
        if not n_line:
            return
        n = int(n_line)
    except (IOError, ValueError):
        return

    if n == 0:
        print(0)
        return

    a = list(map(int, sys.stdin.readline().split()))
    k = int(sys.stdin.readline())

    if k == 1:
        print(max(a))
        return

    low = 0
    high = max(a)
    ans = high
    k_minus_1 = k - 1

    while low <= high:
        t = (low + high) // 2
        radiator_minutes_needed = 0
        for val in a:
            if val > t:
                radiator_minutes_needed += (val - t + k_minus_1 - 1) // k_minus_1

        if radiator_minutes_needed <= t:
            ans = t
            high = t - 1
        else:
            low = t + 1
            
    print(ans)

solve()