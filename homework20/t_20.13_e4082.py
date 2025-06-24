import sys

input = sys.stdin.read

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1, data)

    def build(self, node, start, end, data):
        if start == end:
            if data[start] > 0:
                self.tree[node] = 1
            elif data[start] < 0:
                self.tree[node] = -1
            else:
                self.tree[node] = 0
            return
        mid = (start + end) // 2
        self.build(2 * node + 1, start, mid, data)
        self.build(2 * node + 2, mid + 1, end, data)
        self.tree[node] = self.tree[2 * node + 1] * self.tree[2 * node + 2]

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 1
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left = self.query(2 * node + 1, start, mid, l, r)
        right = self.query(2 * node + 2, mid + 1, end, l, r)
        return left * right

    def update(self, node, start, end, idx, value):
        if start == end:
            if value > 0:
                self.tree[node] = 1
            elif value < 0:
                self.tree[node] = -1
            else:
                self.tree[node] = 0
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node + 1, start, mid, idx, value)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, value)
        self.tree[node] = self.tree[2 * node + 1] * self.tree[2 * node + 2]


def main():
    data = input().splitlines()

    index = 0
    result = []
    while index < len(data):
        n, k = map(int, data[index].split())
        index += 1
        arr = list(map(int, data[index].split()))
        index += 1

        seg_tree = SegmentTree(arr)
        answer = []

        for _ in range(k):
            query = data[index].split()
            index += 1
            if query[0] == 'P':
                i, j = map(int, query[1:])
                product = seg_tree.query(0, 0, n - 1, i - 1, j - 1)
                if product == 0:
                    answer.append('0')
                elif product > 0:
                    answer.append('+')
                else:
                    answer.append('-')
            elif query[0] == 'C':
                i, v = map(int, query[1:])
                seg_tree.update(0, 0, n - 1, i - 1, v)

        result.append(''.join(answer))

    sys.stdout.write("\n".join(result) + "\n")


if __name__ == "__main__":
    main()