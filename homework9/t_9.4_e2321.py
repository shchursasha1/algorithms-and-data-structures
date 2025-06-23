import sys

def solve():
    try:
        n = int(sys.stdin.readline())
        if n == 0:
            return
        
        numbers = list(map(int, sys.stdin.readline().split()))
        numbers.sort()
        
        print(*numbers)
        
    except (IOError, ValueError):
        return

solve()