class Heap:
    def __init__(self):
        self.items = []
        self.id_to_index = {}

    def insert(self, priority, id):
        self.items.append((priority, id))
        index = len(self.items) - 1
        self.id_to_index[id] = index
        self._sift_up(index)

    def extract_max(self):
        if not self.items:
            return None
        max_elem = self.items[0]
        last = self.items.pop()
        del self.id_to_index[max_elem[1]]

        if self.items:
            self.items[0] = last
            self.id_to_index[last[1]] = 0
            self._sift_down(0)

        return max_elem

    def change_priority(self, id, new_priority):
        i = self.id_to_index.get(id)
        if i is None:
            return
        old_priority, _ = self.items[i]
        self.items[i] = (new_priority, id)

        if new_priority > old_priority:
            self._sift_up(i)
        else:
            self._sift_down(i)

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.items[i][0] > self.items[parent][0]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _sift_down(self, i):
        size = len(self.items)
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < size and self.items[left][0] > self.items[largest][0]:
                largest = left
            if right < size and self.items[right][0] > self.items[largest][0]:
                largest = right

            if largest == i:
                break

            self._swap(i, largest)
            i = largest

    def _swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]
        self.id_to_index[self.items[i][1]] = i
        self.id_to_index[self.items[j][1]] = j


class PriorityQueue:
    def __init__(self):
        self.heap = Heap()

    def add(self, id, priority):
        if id in self.heap.id_to_index:
            return
        self.heap.insert(priority, id)

    def pop(self):
        return self.heap.extract_max()

    def change(self, id, new_priority):
        self.heap.change_priority(id, new_priority)


def main():
    import sys
    pq = PriorityQueue()

    for line in sys.stdin:
        parts = line.strip().split()
        if not parts:
            continue
        command = parts[0]

        if command == "ADD":
            id = parts[1]
            priority = int(parts[2])
            pq.add(id, priority)

        elif command == "POP":
            result = pq.pop()
            if result:
                print(f"{result[1]} {result[0]}")

        elif command == "CHANGE":
            id = parts[1]
            new_priority = int(parts[2])
            pq.change(id, new_priority)


if __name__ == "__main__":
    main()