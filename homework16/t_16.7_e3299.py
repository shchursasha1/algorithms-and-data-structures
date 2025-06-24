import sys
from math import log2, floor


def main():
    input = sys.stdin.read().split()
    ptr = 0
    n, m = map(int, input[ptr:ptr + 2])
    ptr += 2

    parent = [0] * n
    children = [[] for _ in range(n)]
    for i in range(1, n):
        p = int(input[ptr])
        ptr += 1
        parent[i] = p
        children[p].append(i)

    LOG = floor(log2(n)) + 1
    up = [[-1] * n for _ in range(LOG)]
    depth = [0] * n

    from collections import deque
    q = deque([0])
    up[0][0] = -1
    depth[0] = 0

    while q:
        v = q.popleft()
        for u in children[v]:
            depth[u] = depth[v] + 1
            up[0][u] = v
            q.append(u)

    # Binary lifting
    for k in range(1, LOG):
        for v in range(n):
            if up[k - 1][v] != -1:
                up[k][v] = up[k - 1][up[k - 1][v]]
            else:
                up[k][v] = -1

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        # Bring u up to depth of v
        for k in range(LOG - 1, -1, -1):
            if depth[u] - (1 << k) >= depth[v]:
                u = up[k][u]
        if u == v:
            return u
        for k in range(LOG - 1, -1, -1):
            if up[k][u] != -1 and up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]
        return up[0][u]

    a1, a2 = map(int, input[ptr:ptr + 2])
    ptr += 2
    x, y, z = map(int, input[ptr:ptr + 3])
    ptr += 3

    a = [0] * (2 * m + 2)
    a[1] = a1
    a[2] = a2
    for i in range(3, 2 * m + 1):
        a[i] = (x * a[i - 2] + y * a[i - 1] + z) % n

    res = 0
    v_prev = 0
    total = 0
    for i in range(1, m + 1):
        u = (a[2 * i - 1] + v_prev) % n
        v = a[2 * i] % n
        v_prev = lca(u, v)
        total += v_prev
    print(total)


if __name__ == '__main__':
    main()