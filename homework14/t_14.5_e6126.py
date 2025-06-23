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

    def exit(self):
        return "bye"

    def clear(self):
        self._front = None
        self._back = None
        self._size = 0
        return "ok"

    def size(self):
        return self._size

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)

if __name__ == "__main__":
    with open("input.txt") as f:
        queue = Queue()
        for line in f:
            if line.split()[0] == "exit":
                print(queue.execute(line))
                break
            print(queue.execute(line))