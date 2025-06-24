import sys
import math

def prim(n, points):
    INF = float('inf')
    total = 0.0
    visited = [False] * n
    min_dist = [INF] * n
    min_dist[0] = 0

    for _ in range(n):
        u = -1
        for v in range(n):
            if not visited[v] and (u == -1 or min_dist[v] < min_dist[u]):
                u = v
        if min_dist[u] == INF:
            return -1  #
        visited[u] = True
        total += math.sqrt(min_dist[u])
        for v in range(n):
            if not visited[v]:
                dx = points[u][0] - points[v][0]
                dy = points[u][1] - points[v][1]
                dist_sq = dx * dx + dy * dy
                if dist_sq < min_dist[v]:
                    min_dist[v] = dist_sq
    return total

def solve_fast():
    input = sys.stdin.read().split()
    ptr = 0
    while True:
        n = int(input[ptr])
        ptr += 1
        if n == 0:
            break
        points = []
        for _ in range(n):
            x = int(input[ptr])
            y = int(input[ptr + 1])
            points.append((x, y))
            ptr += 2
        print("{0:.2f}".format(prim(n, points)))

solve_fast()