import sys
from collections import deque

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    M = int(input[ptr + 1])
    ptr += 2
    adj = [[] for _ in range(N + 1)]

    for _ in range(M):
        i = int(input[ptr])
        j = int(input[ptr + 1])
        ptr += 2
        adj[i].append(j)
        adj[j].append(i)

    visited = [False] * (N + 1)
    components = []

    for node in range(1, N + 1):
        if not visited[node]:
            queue = deque()
            queue.append(node)
            visited[node] = True
            component = []
            while queue:
                current = queue.popleft()
                component.append(current)
                for neighbor in adj[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            components.append(component)

    print(len(components))
    for component in components:
        print(len(component))
        print(' '.join(map(str, sorted(component))) + ' ')

if __name__ == "__main__":
    main()