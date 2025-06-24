def is_heap(arr):
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    if is_heap(arr):
        print("YES")
    else:
        print("NO")