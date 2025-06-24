import math
import sys

input = sys.stdin.read


def lcm(a, b):
    return a * b // math.gcd(a, b)


class SegmentTree:
    def __init__(self, data, operation, identity):
        self.n = len(data)
        self.tree = [identity] * (4 * self.n)
        self.operation = operation
        self.identity = identity
        self._build(data, 0, 0, self.n - 1)

    def _build(self, data, node, l, r):
        if l == r:
            self.tree[node] = data[l]
        else:
            mid = (l + r) // 2
            self._build(data, 2 * node + 1, l, mid)
            self._build(data, 2 * node + 2, mid + 1, r)
            self.tree[node] = self.operation(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, idx, val):
        self._update(0, 0, self.n - 1, idx, val)

    def _update(self, node, l, r, idx, val):
        if l == r:
            self.tree[node] = val
        else:
            mid = (l + r) // 2
            if idx <= mid:
                self._update(2 * node + 1, l, mid, idx, val)
            else:
                self._update(2 * node + 2, mid + 1, r, idx, val)
            self.tree[node] = self.operation(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, ql, qr):
        return self._query(0, 0, self.n - 1, ql, qr)

    def _query(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return self.identity
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        left = self._query(2 * node + 1, l, mid, ql, qr)
        right = self._query(2 * node + 2, mid + 1, r, ql, qr)
        return self.operation(left, right)


def main():
    data = input().split()
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    m = int(data[n+1])
    queries = data[n+2:]

    gcd_tree = SegmentTree(arr, math.gcd, 0)
    lcm_tree = SegmentTree(arr, lcm, 1)

    results = []
    idx = 0
    while idx < len(queries):
        q = int(queries[idx])
        l = int(queries[idx + 1]) - 1
        r = int(queries[idx + 2]) - 1

        if q == 1:
            g = gcd_tree.query(l, r)
            lcm_val = lcm_tree.query(l, r)
            if g < lcm_val:
                results.append("wins")
            elif g > lcm_val:
                results.append("loser")
            else:
                results.append("draw")
        else:
            gcd_tree.update(l, r + 1)
            lcm_tree.update(l, r + 1)
        idx += 3

    print('\n'.join(results))


if __name__ == '__main__':
    main()