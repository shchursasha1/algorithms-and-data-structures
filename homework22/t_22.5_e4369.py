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
    for _ in range(m):
        u = int(input[ptr])
        ptr += 1
        v = int(input[ptr])
        ptr += 1
        adj[u].append(v)
        adj[v].append(u)

    k = int(input[ptr])
    ptr += 1
    sources = list(map(int, input[ptr:ptr + k]))
    ptr += k

    time = [-1] * (n + 1)
    q = deque()

    for node in sources:
        time[node] = 0
        q.append(node)

    last_time = 0
    last_node = sources[0]

    while q:
        current = q.popleft()
        for neighbor in adj[current]:
            if time[neighbor] == -1:
                time[neighbor] = time[current] + 1
                q.append(neighbor)
                if time[neighbor] > last_time:
                    last_time = time[neighbor]
                    last_node = neighbor
                elif time[neighbor] == last_time and neighbor < last_node:
                    last_node = neighbor

    if last_time == 0:
        last_node = min(sources)

    print(last_time)
    print(last_node)

if __name__ == "__main__":
    main()