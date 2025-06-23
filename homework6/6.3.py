"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

EMPTY = "EMPTY"
DELETED = "DELETED"

M: int = 31
size: int = 1000003
count: int
authors: list
books: list


def hash_function(s):
    """ Поліноміальна хеш-функція """
    h = 0
    for char in s:
        h = h * M + ord(char)
    return h % size


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global count, authors, books
    count = 0
    authors = [EMPTY] * size
    books = [EMPTY] * size


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global count

    i = hash_function(author)
    j = -1

    while authors[i] is not EMPTY:
        if authors[i] == author:
            if books[i] is EMPTY:
                books[i] = []
            books[i].append(title)
            return
        if authors[i] is DELETED:
            j = i
        i = (i + 1) % size

    if j == -1:
        j = i
        count += 1

    authors[j] = author
    books[j] = [title]


def find(author, title):
    """ Перевіряє, чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга є, False якщо немає
    """
    i = hash_function(author)

    while authors[i] is not EMPTY:
        if authors[i] == author:
            return title in books[i]
        i = (i + 1) % size
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    global count

    i = hash_function(author)
    while authors[i] is not EMPTY:
        if authors[i] == author:
            if books[i] and title in books[i]:
                books[i].remove(title)

                if not books[i]:
                    authors[i] = DELETED
                    books[i] = EMPTY
                    count -= 1
                return
        i = (i + 1) % size


def findByAuthor(author):
    """ Повертає список книг автора у алфавітному порядку.
    Якщо книг немає, повертає порожній список.
    :param author: Автор
    :return: Відсортований список книг автора.
    """
    i = hash_function(author)
    while authors[i] is not EMPTY:
        if authors[i] == author:
            if books[i] is not EMPTY:
                return sorted(books[i])
            else:
                return []
        i = (i + 1) % size
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
