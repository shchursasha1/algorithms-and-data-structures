class Tree:
    def __init__(self, key, cost, parent=None):
        self.key = key
        self.cost = cost
        self.children = []
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)


def build_tree(data):
    nodes = {}
    for key in data:
        cost, k, *subordinates = data[key]
        nodes[key] = Tree(key, cost)

    for key in data:
        cost, k, *subordinates = data[key]
        current_node = nodes[key]
        for child_key in subordinates:
            child_node = nodes[child_key]
            child_node.parent = current_node
            current_node.add_child(child_node)
    root = None
    for key in nodes:
        if nodes[key].parent is None:
            root = nodes[key]
            break
    return root


def minimal_license_cost(node):
    if not node.children:
        return node.cost
    min_child_cost = min(minimal_license_cost(child) for child in node.children)
    return node.cost + min_child_cost


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    N = int(lines[0].strip())
    data = {}
    for i in range(1, N + 1):
        parts = list(map(int, lines[i].strip().split()))
        cost = parts[0]
        k = parts[1]
        subordinates = parts[2:]
        data[i] = (cost, k, *subordinates)

    root = build_tree(data)

    if root is None:
        print("Помилка: не знайдено корінь дерева (міністра)")
        return

    print(minimal_license_cost(root))


if __name__ == "__main__":
    main()