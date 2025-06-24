n, m = map(int, input().split())
in_degree = [0] * (n + 1)
out_degree = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    out_degree[u] += 1
    in_degree[v] += 1

for i in range(1, n + 1):
    print(in_degree[i], out_degree[i])