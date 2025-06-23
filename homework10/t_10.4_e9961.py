def sequences(lst : list, n, k):
    l = len(lst)

    if l == k:
        print(*lst)
        return

    for i in range(1, n + 1):
        if i not in lst:
            lst_next = lst[:]
            lst_next.append(i)
            sequences(lst_next, n, k)


if __name__ == "__main__":
    n, k = map(int, input().split())
    lst = []
    sequences(lst, n, k)