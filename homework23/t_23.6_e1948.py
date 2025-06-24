import sys
from collections import deque


def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    m = int(input[ptr + 1])
    ptr += 2
    adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    for _ in range(m):
        u = int(input[ptr])
        v = int(input[ptr + 1])
        ptr += 2
        adj[u].append(v)
        in_degree[v] += 1

    queue = deque()
    for u in range(1, n + 1):
        if in_degree[u] == 0:
            queue.append(u)

    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(topo_order) != n:
        print(-1)
    else:
        print(' '.join(map(str, topo_order)))


if __name__ == "__main__":
    main()