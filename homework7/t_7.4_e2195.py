import math
import re
import sys

EMPTY = None


def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class Set:

    M = 31
    def __init__(self, size=1000003):
        self._size = size
        self.count = 0
        self._keys: list[EMPTY | str] = [EMPTY] * size

    def _rehash(self):

        self._size = self._size * 2 + 1
        while not is_prime(self._size):
            self._size += 2

        old_keys = self._keys
        self.__init__(self._size)

        for key in old_keys:
            if key is not EMPTY:
                self.add(key)

    def hash(self, s):

        h = 0
        for char in s:
            h = h * self.M + ord(char)
        return h % self._size

    def add(self, key: str):
        if self._size * 0.7 < self.count:
            self._rehash()

        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return
            i = (i + 1) % self._size

        self.count += 1
        self._keys[i] = key

    def get(self, key):
        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return True
            i = (i + 1) % self._size
        return False

    def keys(self):
        return [key for key in self._keys if key is not EMPTY]

def case_1(words: Set, text: set):
    for word in text:
        if not words.get(word):
            return False
    return True

def case_2(words: Set, text: set):
    for word in words.keys():
        if word not in text:
            return False
    return True

def main():
    try:
        N, M = map(int, sys.stdin.readline().split())
    except (IOError, ValueError):
        N, M = 0, 0
    
    words = Set()
    for _ in range(N):
        words.add(sys.stdin.readline().strip().lower())

    text_list = []
    for _ in range(M):
        line = sys.stdin.readline().strip().lower()
        line = re.sub(r"[.,:;\'\"!?-]", " ", line)
        text_list.extend(line.split())
    text = set(text_list)

    if not case_1(words, text):
        print("Some words from the text are unknown.")

    elif not case_2(words, text):
        print("The usage of the vocabulary is not perfect.")
        
    else:
        print("Everything is going to be OK.")


main()