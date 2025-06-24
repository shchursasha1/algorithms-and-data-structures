class Node:
    def __init__(self, node_id, is_leaf=False, result=None):
        self.node_id = node_id
        self.is_leaf = is_leaf
        self.result = result
        self.children = []

def minimax(node, depth):
    if node.is_leaf:
        return node.result

    if depth % 2 == 0:
        return max(minimax(child, depth + 1) for child in node.children)
    else:
        return min(minimax(child, depth + 1) for child in node.children)

def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    n = int(lines[0])
    nodes = {i: Node(i) for i in range(1, n + 1)}

    for i in range(2, n + 1):
        parts = lines[i - 1].split()
        node_type = parts[0]
        parent_id = int(parts[1])

        if node_type == 'L':
            result = int(parts[2])
            nodes[i].is_leaf = True
            nodes[i].result = result

        nodes[parent_id].children.append(nodes[i])

    result = minimax(nodes[1], 0)

    if result == 0:
        print("0")
    else:
        print(f"{result:+d}")

if __name__ == "__main__":
    main()
