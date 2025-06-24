import heapq

def dijkstra(n, graph, start, end):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0

    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)

        if current_dist > distances[current_vertex]:
            continue

        for neighbor in range(1, n + 1):
            weight = graph[current_vertex - 1][neighbor - 1]
            if weight != -1 and weight != 0:
                distance = current_dist + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances[end] if distances[end] != float('inf') else -1


n, s, f = map(int, input().split())
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

result = dijkstra(n, graph, s, f)
print(result)