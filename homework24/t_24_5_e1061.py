import sys
from collections import deque

def readints():
    return map(int, sys.stdin.readline().split())

n, m = readints()
g = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
INF = 10**18

def bfs(ch):
    dist = [[INF]*m for _ in range(n)]
    dq = deque()
    for i in range(n):
        for j in range(m):
            if g[i][j] == ch:
                dist[i][j] = 0
                dq.append((i, j))
    while dq:
        x, y = dq.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] != '#':
                w = 1 if g[nx][ny] == '.' else 0
                nd = dist[x][y] + w
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    if w:
                        dq.append((nx, ny))
                    else:
                        dq.appendleft((nx, ny))
    return dist

d1 = bfs('1')
d2 = bfs('2')
d3 = bfs('3')
ans = INF
for i in range(n):
    for j in range(m):
        if g[i][j] != '#' and d1[i][j] < INF and d2[i][j] < INF and d3[i][j] < INF:
            total = d1[i][j] + d2[i][j] + d3[i][j]
            if g[i][j] == '.':
                total -= 2
            if total < ans:
                ans = total
print(-1 if ans == INF else ans)
