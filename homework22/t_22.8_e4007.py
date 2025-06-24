from collections import deque


def operations(number):
    num_str = str(number)
    operations_list = []

    if num_str[0] != '9':
        new_num = str(int(num_str[0]) + 1) + num_str[1:]
        operations_list.append(int(new_num))

    if num_str[-1] != '1':
        new_num = num_str[:-1] + str(int(num_str[-1]) - 1)
        operations_list.append(int(new_num))

    shifted_right = num_str[-1] + num_str[:-1]
    operations_list.append(int(shifted_right))

    shifted_left = num_str[1:] + num_str[0]
    operations_list.append(int(shifted_left))

    return operations_list


def find_shortest_path(start, end):
    if start == end:
        return [start]

    queue = deque()
    queue.append(start)
    visited = {}
    visited[start] = (None, None)

    while queue:
        current = queue.popleft()

        for neighbor in operations(current):
            if neighbor not in visited:
                visited[neighbor] = (current, None)
                queue.append(neighbor)
                if neighbor == end:

                    path = []
                    node = neighbor
                    while node is not None:
                        path.append(node)
                        node, _ = visited.get(node, (None, None))
                    return path[::-1]

    return []


def main():
    start = int(input().strip())
    end = int(input().strip())

    path = find_shortest_path(start, end)

    for number in path:
        print(number)


if __name__ == "__main__":
    main()