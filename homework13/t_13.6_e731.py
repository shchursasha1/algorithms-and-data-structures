class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self, maxsize=100):
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

    def is_empty(self):
        return self.top is None

def is_operator(c):
    return c in '+-*/'

def precedence(op):
    if op in '*/':
        return 2
    elif op in '+-':
        return 1
    return 0

def prefix_to_infix(prefix):
    stack = Stack()

    for char in reversed(prefix):
        if not is_operator(char):
            stack.push(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()

            if isinstance(operand1, tuple):
                op1, prec1 = operand1
                if precedence(char) > prec1:
                    operand1_str = f"({op1})"
                else:
                    operand1_str = op1
            else:
                operand1_str = operand1

            if isinstance(operand2, tuple):
                op2, prec2 = operand2
                if precedence(char) > prec2 or (char in '-/' and precedence(char) == prec2):
                    operand2_str = f"({op2})"
                else:
                    operand2_str = op2
            else:
                operand2_str = operand2
            new_expr = f"{operand1_str}{char}{operand2_str}"
            stack.push((new_expr, precedence(char)))

    result = stack.pop()
    if isinstance(result, tuple):
        return result[0]
    return result

if __name__ == "__main__":
    prefix_expr = input().strip()
    infix_expr = prefix_to_infix(prefix_expr)
    print(infix_expr)