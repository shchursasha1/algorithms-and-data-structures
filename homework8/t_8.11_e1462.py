def help_func(a, b):
    if a == b:
        return False

    last_a = a % 10
    last_b = b % 10

    if last_a == last_b:
        return a > b
    return last_a > last_b


# використаний алгоритм сортування вибором
def sort(arr):
    n = len(arr)
    for j in range(n, 0, -1):
        pos = 0
        for i in range(1, j):
            if help_func(arr[i], arr[pos]):
                pos = i
        arr[pos], arr[j - 1] = arr[j - 1], arr[pos]

    return arr


n = int(input())
arr = []
for i in range(n):
     arr.append(int(input()))

print(*sort(arr))