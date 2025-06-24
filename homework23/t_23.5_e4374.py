import sys
from sys import stdin


def main():
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read().split()
    ptr = 0
    N, M = int(input[ptr]), int(input[ptr + 1])
    ptr += 2
    edges = []
    adj = [[] for _ in range(N + 1)]
    for i in range(M):
        a, b = int(input[ptr]), int(input[ptr + 1])
        ptr += 2
        edges.append((a, b))
        adj[a].append((b, i + 1))
        adj[b].append((a, i + 1))

    K = int(input[ptr])
    ptr += 1
    queries = []
    for _ in range(K):
        parts = list(map(int, input[ptr:ptr + 1 + int(input[ptr])]))
        queries.append(parts)
        ptr += 1 + parts[0]

    for query in queries:
        C = query[0]
        removed_edges = set(query[1:])
        parent = [i for i in range(N + 1)]
        rank = [1] * (N + 1)

        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        def union(u, v):
            u_root = find(u)
            v_root = find(v)
            if u_root == v_root:
                return
            if rank[u_root] > rank[v_root]:
                parent[v_root] = u_root
                rank[u_root] += rank[v_root]
            else:
                parent[u_root] = v_root
                rank[v_root] += rank[u_root]

        for i in range(M):
            edge_num = i + 1
            if edge_num not in removed_edges:
                a, b = edges[i]
                union(a, b)

        root = find(1)
        connected = True
        for u in range(2, N + 1):
            if find(u) != root:
                connected = False
                break
        print("Connected" if connected else "Disconnected")


if __name__ == "__main__":
    main()