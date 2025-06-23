class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        if self.top is None:
            return "error"
        item = self.top.item
        self.top = self.top.next
        self._size -= 1
        return item

    def back(self):
        if self.top is None:
            return "error"
        return self.top.item


    def is_empty(self):
        return self.top is None

def is_possible_to_rearrange(n, target_sequence):
    stack = Stack()
    current_wagon = 1
    for target in target_sequence:
        while current_wagon <= n and (stack.is_empty() or stack.back() != target):
            stack.push(current_wagon)
            current_wagon += 1
        if not stack.is_empty() and stack.back() == target:
            stack.pop()
        else:
            return False
    return True

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            n = int(line)
            if n == 0:
                break
            while True:
                line = f.readline().strip()
                if not line or line == "0":
                    print()
                    break
                sequence = list(map(int, line.split()))
                if is_possible_to_rearrange(n, sequence):
                    print("Yes")
                else:
                    print("No")