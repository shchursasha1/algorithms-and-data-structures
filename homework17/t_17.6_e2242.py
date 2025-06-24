import sys
sys.setrecursionlimit(1500)

class Btree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, node):
        if node.key < self.key:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)

    def print(self):
        print(self.key, end="")
        if self.left is not None:
            self.left.print()
        if self.right is not None:
            self.right.print()


if __name__ == "__main__":
    with open("input.txt") as file:
        nodes = []
        for line in file:
            if line.strip() == "*":
                break
            nodes.append(line.strip())

    all_nodes = []
    for line in reversed(nodes):
        all_nodes.extend(line)

    root = None
    for ch in all_nodes:
        node = Btree(ch)
        if root is None:
            root = node
        else:
            root.insert(node)

    root.print()