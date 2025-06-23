BRACKETS = {'(': ')', '[': ']', '{': '}'}

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:

    def __init__(self, maxsize = 100):
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

    def size(self):
        return self._size

def check(brackets):
    stack = Stack()
    for bracket in brackets:
        if bracket in BRACKETS:
            stack.push(bracket)
        else:
            if stack.size() > 0:
                el = stack.pop()
                if BRACKETS[el] != bracket:
                    return "no"
            else:
                return "no"
    if stack.size() > 0:
        return "no"
    return "yes"


if __name__ == "__main__":
    brackets = input()
    print(check(brackets))