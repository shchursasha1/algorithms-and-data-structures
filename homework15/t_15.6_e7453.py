class Node:

    def __init__(self, data: int):
        self.data: int = data
        self.next: [Node | None] = None

class List:

    def __init__(self):
        self.head: [Node | None] = None
        self.tail: [Node | None] = None

    def addToTail(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node
        return

    def Print(self) -> None:
        elems = []
        node = self.head
        while node is not None:
            elems.append(node.data)
            node = node.next
        print(*elems, sep=' ')

    def RotateRight(self, k: int) -> None:
        if self.head is None or k == 0:
            return

        length = 1
        current = self.head
        while current.next is not None:
            current = current.next
            length += 1

        k = k % length
        if k == 0:
            return

        new_tail_pos = length - k - 1
        new_tail = self.head
        for _ in range(new_tail_pos):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        self.tail.next = self.head
        self.head = new_head
        self.tail = new_tail


if __name__ == "__main__":
    with open("input.txt") as file:
        n = file.readline()
        elems = [int(el) for el in file.readline().split()]
        list = List()
        for el in elems:
            list.addToTail(el)

        for k in file.readlines():
            if k != '\n':
                list.RotateRight(int(k))
                list.Print()