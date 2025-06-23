class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def push_front(self, item):
        node = Node(item)
        if self._size == 0:
            self._front = node
            self._back = node
        else:
            node.next = self._front
            self._front.prev = node
            self._front = node
        self._size += 1
        return "ok"

    def push_back(self, item):
        node = Node(item)
        if self._size == 0:
            self._front = node
            self._back = node
        else:
            node.prev = self._back
            self._back.next = node
            self._back = node
        self._size += 1
        return "ok"

    def pop_front(self):
        if self._size == 0:
            return "error"
        item = self._front.data
        self._front = self._front.next
        if self._front is not None:
            self._front.prev = None
        else:
            self._back = None
        self._size -= 1
        return item

    def pop_back(self):
        if self._size == 0:
            return "error"
        item = self._back.data
        self._back = self._back.prev
        if self._back is not None:
            self._back.next = None
        else:
            self._front = None
        self._size -= 1
        return item

    def front(self):
        if self._size == 0:
            return "error"
        return self._front.data

    def back(self):
        if self._size == 0:
            return "error"
        return self._back.data

    def size(self):
        return self._size

    def clear(self):
        self._front = None
        self._back = None
        self._size = 0
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)

if __name__ == "__main__":
    with open("input.txt") as f:
        queue = Deque()
        for line in f:
            if line.split()[0] == "exit":
                print(queue.execute(line))
                break
            print(queue.execute(line))