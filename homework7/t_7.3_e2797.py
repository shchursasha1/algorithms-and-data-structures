import math
import sys

EMPTY = None


def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class Set:

    M = 31

    def __init__(self, size=100003):
        self._size = size
        self._count = 0
        self._keys: list[EMPTY | str] = [EMPTY for _ in range(size)]

    def _rehash(self):
        new_size = self._size * 2
        while not is_prime(new_size):
            new_size += 1

        old_keys = self._keys
        self.__init__(new_size)
        
        for key in old_keys:
            if key is not EMPTY:
                self.add(key)

    def hash(self, s):
        h = 0
        for i in range(len(s)):
            h = (h * self.M + ord(s[i]))
        return h % self._size

    def add(self, key: str):
        if self._size * 0.7 < self._count:
            self._rehash()

        i = self.hash(key)
        start_index = i
        
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return
            i = (i + 1) % self._size
            if i == start_index: 
                self._rehash()
                self.add(key)
                return

        self._count += 1
        self._keys[i] = key

    def __iter__(self):
        res = []
        for i in range(self._size):
            if self._keys[i] is not EMPTY:
                res.append(self._keys[i])
        return iter(res)


def main():
    try:
        sys.stdin.readline()
        numbers = sys.stdin.readline().split()
    except (IOError, ValueError):
        numbers = []

    res = Set()
    for number in numbers:
        res.add(number)
    print(res._count)


main()