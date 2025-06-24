import math
import sys

input = sys.stdin.read


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(data, 0, 0, self.n - 1)

    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(data, left_child, start, mid)
            self.build(data, right_child, mid + 1, end)
            self.tree[node] = math.gcd(self.tree[left_child], self.tree[right_child])

    def update(self, index, value, node, start, end):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if start <= index <= mid:
                self.update(index, value, left_child, start, mid)
            else:
                self.update(index, value, right_child, mid + 1, end)
            self.tree[node] = math.gcd(self.tree[left_child], self.tree[right_child])

    def query(self, l, r, node, start, end):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_query = self.query(l, r, left_child, start, mid)
        right_query = self.query(l, r, right_child, mid + 1, end)
        return math.gcd(left_query, right_query)

    def update_value(self, index, value):
        self.update(index, value, 0, 0, self.n - 1)

    def gcd(self, l, r):
        return self.query(l, r, 0, 0, self.n - 1)


def main():
    data = input().split()
    n = int(data[0])
    arr = list(map(int, data[1:n + 1]))
    m = int(data[n + 1])
    queries = data[n + 2:]

    tree = SegmentTree(arr)
    index = 0
    res = []

    while index < len(queries):
        q = int(queries[index])
        l = int(queries[index + 1]) - 1
        r = int(queries[index + 2]) - 1

        if q == 1:
            res_fin = tree.gcd(l, r)
            res.append(res_fin)
        elif q == 2:
            tree.update_value(l, r + 1)

        index += 3

    for res_fin in res:
        print(res_fin)


if __name__ == "__main__":
    main()