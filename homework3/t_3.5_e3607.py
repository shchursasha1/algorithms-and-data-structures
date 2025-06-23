import sys

def solve():
    for n_line in sys.stdin:
        n_line = n_line.strip()
        if not n_line:
            continue

        heights = map(int, sys.stdin.readline().split())
        a, b = map(int, sys.stdin.readline().split())

        count = sum(1 for h in heights if a <= h <= b)
        
        print(count)

solve()