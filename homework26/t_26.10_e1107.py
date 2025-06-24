import heapq

def find_mst_prim(n, edges, exclude_edge=None):
    adj = [[] for _ in range(n)]
    for i, (u, v, w) in enumerate(edges):
        if exclude_edge is not None and i == exclude_edge:
            continue
        adj[u].append((w, v, i))
        adj[v].append((w, u, i))

    used = [False] * n
    min_heap = []
    used[0] = True
    for w, v, i in adj[0]:
        heapq.heappush(min_heap, (w, v, i))

    mst_cost = 0
    mst_edges = []
    while min_heap and len(mst_edges) < n - 1:
        w, u, i = heapq.heappop(min_heap)
        if not used[u]:
            used[u] = True
            mst_cost += w
            mst_edges.append(i)
            for nw, nv, ni in adj[u]:
                if not used[nv]:
                    heapq.heappush(min_heap, (nw, nv, ni))

    if len(mst_edges) < n - 1:
        return float('inf'), []
    return mst_cost, mst_edges


def two_best_mst_costs(n, m, edge_list):
    edges = [(a - 1, b - 1, c) for a, b, c in edge_list]

    s1, mst_edges = find_mst_prim(n, edges)

    s2 = float('inf')
    for idx in mst_edges:
        cost, _ = find_mst_prim(n, edges, exclude_edge=idx)
        if cost != float('inf') and cost < s2:
            if cost == s1:
                s2 = s1
            elif cost > s1:
                s2 = min(s2, cost)

    return s1, s2


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))

    s1, s2 = two_best_mst_costs(n, m, edges)
    print(s1, s2)
