"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

class Node:
    def __init__(self, author: str, books: list[str]):
        self.author: str = author
        self.books: list[str] = books
        self.next: [None | Node] = None


M: int = 31
size: int = 1000003
authors: list[None | Node]


def hash_function(s):
    """ Поліноміальна хеш-функція """
    h = 0
    for char in s:
        h = h * M + ord(char)
    return h % size


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global authors
    authors = [None for _ in range(size)]


def addBook(author, title):
    """ Додає книгу до бібліотеки. """
    i = hash_function(author)
    node = authors[i]

    while node is not None:
        if node.author == author:
            if title not in node.books:
                node.books.append(title)
            return
        node = node.next

    new_node = Node(author, [title])
    new_node.next = authors[i]
    authors[i] = new_node


def find(author, title):
    """ Перевіряє, чи міститься задана книга у бібліотеці. """
    i = hash_function(author)
    node = authors[i]

    while node is not None:
        if node.author == author:
            return title in node.books
        node = node.next
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки. """
    i = hash_function(author)
    node = authors[i]
    prev = None

    while node is not None:
        if node.author == author:
            if title in node.books:
                node.books.remove(title)
                if not node.books:  # Якщо список книг порожній, видаляємо вузол
                    if prev is None:  # Видаляємо перший елемент у списку
                        authors[i] = node.next
                    else:
                        prev.next = node.next
                return
        prev = node
        node = node.next


def findByAuthor(author):
    """ Повертає список книг автора у алфавітному порядку. """
    i = hash_function(author)
    node = authors[i]

    while node is not None:
        if node.author == author:
            return sorted(node.books)
        node = node.next
    return []


if __name__ == "__main__":
    init()
    addBook("Sasha", "Witcher 1")
    addBook("Sasha", "Witcher 2")
    addBook("Alice", "Wonderland")
    delete("Sasha", "Witcher 1")

    print(find("Sasha", "Witcher 1"))  # False
    print(find("Sasha", "Witcher 2"))  # True
    print(findByAuthor("Sasha"))  # ['Witcher 2']
    print(findByAuthor("Alice"))  # ['Wonderland']
    print(findByAuthor("Unknown"))  # []