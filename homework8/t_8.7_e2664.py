# використаний алгоритм сортування вставкою
def sort(arr):
    n = len(arr)
    sorted_flag = True

    for i in range(1, n):
        pos = i
        x = arr[pos]
        while pos > 0:
            if arr[pos - 1] > x:
                arr[pos] = arr[pos - 1]
            else:
                break
            pos -= 1
        arr[pos] = x

        if pos != i:
            sorted_flag = False
            print(*arr)

    if sorted_flag:
        return


n = int(input())
arr = list(map(int, input().split()))
sort(arr)