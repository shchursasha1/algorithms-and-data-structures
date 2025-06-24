import sys
from collections import deque

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    m = int(input[ptr])
    ptr += 1

    adj = [[] for _ in range(n + 1)]
    edges = set()
    for _ in range(m):
        u = int(input[ptr])
        ptr += 1
        v = int(input[ptr])
        ptr += 1
        adj[u].append(v)
        adj[v].append(u)
        edges.add((min(u, v), max(u, v)))

    visited = [False] * (n + 1)
    parent = [0] * (n + 1)
    q = deque()
    q.append(1)
    visited[1] = True
    tree_edges = []

    while q:
        current = q.popleft()
        for neighbor in adj[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current
                tree_edges.append((min(current, neighbor), max(current, neighbor)))
                q.append(neighbor)

    for edge in tree_edges:
        print(edge[0], edge[1])

if __name__ == "__main__":
    main()