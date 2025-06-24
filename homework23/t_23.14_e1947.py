import sys
from collections import defaultdict, deque


def main():
    sys.setrecursionlimit(1 << 25)
    n, m = map(int, sys.stdin.readline().split())
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    edges = []
    for _ in range(m):
        b, e = map(int, sys.stdin.readline().split())
        adj[b].append(e)
        rev_adj[e].append(b)
        edges.append((b, e))

    visited = [False] * (n + 1)
    order = []
    for node in range(1, n + 1):
        if not visited[node]:
            stack = [(node, False)]
            while stack:
                current, processed = stack.pop()
                if processed:
                    order.append(current)
                    continue
                if visited[current]:
                    continue
                visited[current] = True
                stack.append((current, True))
                for neighbor in adj[current]:
                    if not visited[neighbor]:
                        stack.append((neighbor, False))

    visited = [False] * (n + 1)
    component = [0] * (n + 1)
    current_component = 0
    for node in reversed(order):
        if not visited[node]:
            stack = [node]
            visited[node] = True
            current_component += 1
            component[node] = current_component
            while stack:
                current = stack.pop()
                for neighbor in rev_adj[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        component[neighbor] = current_component
                        stack.append(neighbor)

    condensation_edges = set()
    for b, e in edges:
        cb = component[b]
        ce = component[e]
        if cb != ce:
            condensation_edges.add((cb, ce))

    print(len(condensation_edges))


if __name__ == '__main__':
    main()