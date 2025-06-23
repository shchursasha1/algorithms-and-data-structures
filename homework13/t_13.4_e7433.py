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


def decimal_to_base(A, P):
    stack = Stack()
    A = int(A)
    P = int(P)

    if A == 0:
        return "0"

    while A > 0:
        remainder = A % P
        stack.push(remainder)
        A = A // P

    result = []
    while stack._size > 0:
        digit = stack.pop()
        if digit < 10:
            result.append(str(digit))
        else:
            result.append(f"[{digit}]")

    return ''.join(result)

A = input()
P = input()
print(decimal_to_base(A, P))