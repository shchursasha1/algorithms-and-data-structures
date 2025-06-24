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

    def PrintReverse(self) -> None:
        elems = []
        node = self.head
        while node is not None:
            elems.append(node.data)
            node = node.next
        print(*elems[::-1], sep=' ')


if __name__ == "__main__":
    n = input()
    nums = input().split()
    list = List()
    for el in nums:
        list.addToTail(int(el))

    list.Print()
    list.PrintReverse()
