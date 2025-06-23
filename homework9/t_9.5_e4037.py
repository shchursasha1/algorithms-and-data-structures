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
        return
        
    robots = []
    for _ in range(n):
        robots.append(list(map(int, sys.stdin.readline().split())))

    robots.sort(key=lambda robot: robot[0])

    for robot in robots:
        sys.stdout.write(f"{robot[0]} {robot[1]}\n")

solve()