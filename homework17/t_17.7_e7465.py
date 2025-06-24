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

    def structure(self):
        res = [self.key]
        if self.left:
            res += self.left.structure()
        else:
            res += ['#']
        if self.right:
            res += self.right.structure()
        else:
            res += ['#']
        return res

def compare_trees(tree1, tree2):
    return tree1.structure() == tree2.structure()


if __name__ == "__main__":
    n1 = int(input())
    nodes_1 = [int(el) for el in input().split()]
    n2 = int(input())
    nodes_2 = [int(el) for el in input().split()]

    root_1 = None
    for el in nodes_1:
        node = Btree(el)
        if root_1 is None:
            root_1 = node
        else:
            root_1.insert(node)

    root_2 = None
    for el in nodes_2:
        node = Btree(el)
        if root_2 is None:
            root_2 = node
        else:
            root_2.insert(node)

    if compare_trees(root_1, root_2):
        print(1)
    else:
        print(0)