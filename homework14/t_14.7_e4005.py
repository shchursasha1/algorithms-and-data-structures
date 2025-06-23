class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def push(self, item):
        node = Node(item)
        if self._size == 0:
            self._front = node
            self._back = node
        else:
            self._back.next = node
            self._back = node
        self._size += 1
        return "ok"

    def pop(self):
        if self._front is None:
            return "error"
        item = self._front.data
        self._front = self._front.next
        self._size -= 1
        if self._size == 0:
            self._back = None
        return item

    def front(self):
        if self._front is None:
            return "error"
        return self._front.data

    def clear(self):
        self._front = None
        self._back = None
        self._size = 0
        return "ok"

    def size(self):
        return self._size


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())

        q1 = Queue()
        q2 = Queue()
        rounds = 0

        line_1 = [int(el) for el in f.readline().split()]
        line_2 = [int(el) for el in f.readline().split()]

        for el in line_1:
            q1.push(el)
        for el in line_2:
            q2.push(el)

        while rounds < 200000:
            if q1.size() == 0:
                print(f"second {rounds}")
                break
            if q2.size() == 0:
                print(f"first {rounds}")
                break
            a = q1.pop()
            b = q2.pop()
            if a == 0 and b == n - 1:
                q1.push(a)
                q1.push(b)
            elif a == n - 1 and b == 0:
                q2.push(a)
                q2.push(b)
            elif a > b:
                q1.push(a)
                q1.push(b)
            else:
                q2.push(a)
                q2.push(b)

            rounds += 1
        else:
            print("draw")