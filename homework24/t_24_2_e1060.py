import sys
from collections import deque

def solve():
    try:
        n_line = sys.stdin.readline()
        if not n_line:
            return
        n = int(n_line)
    except (IOError, ValueError):
        return

    grid = [list(sys.stdin.readline().strip()) for _ in range(n)]

    start_pos = None
    end_pos = None
    for r in range(n):
        for c in range(n):
            if grid[r][c] == '@':
                start_pos = (r, c)
            elif grid[r][c] == 'X':
                end_pos = (r, c)

    q = deque([start_pos])
    visited = {start_pos}
    parent = {start_pos: None}
    path_found = False

    while q:
        r, c = q.popleft()

        if (r, c) == end_pos:
            path_found = True
            break

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                if grid[nr][nc] != 'O':
                    visited.add((nr, nc))
                    parent[(nr, nc)] = (r, c)
                    q.append((nr, nc))

    if not path_found:
        print('N')
    else:
        print('Y')
        curr = end_pos
        while curr is not None and curr != start_pos:
            r, c = curr
            grid[r][c] = '+'
            curr = parent.get(curr)
        
        if start_pos:
             grid[start_pos[0]][start_pos[1]] = '@'

        for row in grid:
            print("".join(row))

solve()