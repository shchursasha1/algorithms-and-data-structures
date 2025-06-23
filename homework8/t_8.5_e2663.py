# використаний алгоритм сортування бульбашкою
def sort(arr):
    count = 0
    n = len(arr)

    for j in range(n - 1, 0, -1):
        temp = 0
        for i in range(j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                count += 1
                temp += 1
        if temp == 0:
            break
    return count


n = int(input())
arr = list(map(int, input().split()))
print(sort(arr))