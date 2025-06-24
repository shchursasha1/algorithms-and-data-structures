import sys

input = sys.stdin.read


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [(0, 0)] * (4 * self.n)
        self._build(data, 0, 0, self.n - 1)

    def _build(self, data, node, l, r):
        if l == r:
            self.tree[node] = (data[l], data[l])
        else:
            mid = (l + r) // 2
            self._build(data, 2 * node + 1, l, mid)
            self._build(data, 2 * node + 2, mid + 1, r)
            self.tree[node] = self._combine(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def _combine(self, left, right):
        return min(left[0], right[0]), max(left[1], right[1])

    def update(self, index, value):
        self._update(0, 0, self.n - 1, index, value)

    def _update(self, node, l, r, index, value):
        if l == r:
            self.tree[node] = (value, value)
        else:
            mid = (l + r) // 2
            if index <= mid:
                self._update(2 * node + 1, l, mid, index, value)
            else:
                self._update(2 * node + 2, mid + 1, r, index, value)
            self.tree[node] = self._combine(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, ql, qr):
        return self._query(0, 0, self.n - 1, ql, qr)

    def _query(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return float('inf'), float('-inf')
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        left = self._query(2 * node + 1, l, mid, ql, qr)
        right = self._query(2 * node + 2, mid + 1, r, ql, qr)
        return self._combine(left, right)


def compute_a(n):
    return (n * n % 12345) + (n * n * n % 23456)


def main():
    data = input().split()
    k = int(data[0])
    queries = data[1:]

    N = 100000
    arr = [compute_a(i + 1) for i in range(N)]
    st = SegmentTree(arr)

    results = []
    index = 0
    while index < len(queries):
        x = int(queries[index])
        y = int(queries[index + 1])
        if x > 0:
            l = x - 1
            r = y - 1
            qmin, qmax = st.query(l, r)
            results.append(str(qmax - qmin))
        else:
            st.update(-x - 1, y)
        index += 2

    print("\n".join(results))


if __name__ == '__main__':
    main()