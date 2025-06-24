def bellman_ford(n, edges, start):
    INF = 30000
    distances = [INF] * (n + 1)
    distances[start] = 0

    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if distances[u] != INF and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                updated = True
        if not updated:
            break

    return distances


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1

    edges = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((u, v, w))

    distances = bellman_ford(n, edges, 1)

    for i in range(1, n + 1):
        print(distances[i], end=(' ' if i < n else '\n'))


if __name__ == "__main__":
    main()