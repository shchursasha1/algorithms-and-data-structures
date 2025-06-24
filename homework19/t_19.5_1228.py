class Heap:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)
        self._sift_up(len(self.data) - 1)

    def extract(self):
        if len(self.data) == 1:
            return self.data.pop()
        top = self.data[0]
        self.data[0] = self.data.pop()
        self._sift_down(0)
        return top

    def __len__(self):
        return len(self.data)

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i] < self.data[parent]:
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else:
                break

    def _sift_down(self, i):
        size = len(self.data)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < size and self.data[left] < self.data[smallest]:
                smallest = left
            if right < size and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == i:
                break

            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest


def min_cost(numbers):
    heap = Heap()
    for num in numbers:
        heap.insert(num)

    total_cost = 0
    while len(heap) > 1:
        a = heap.extract()
        b = heap.extract()
        cost = a + b
        total_cost += cost
        heap.insert(cost)

    return total_cost


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))

    result = min_cost(numbers)
    print(result)