import sys

max_len = 0

def solve(n, arr):
    global max_len
    max_len = 0
    total_sum = sum(arr)

    if total_sum <= n:
        max_len = total_sum
        return total_sum

    if n in arr:
        max_len = n
        return n
    
    for i in range(len(arr)):
        _solve(arr, arr[i], i + 1, n)

    return max_len


def _solve(arr, current_sum, index, n):
    global max_len

    if current_sum > n:
        return

    if current_sum > max_len:
        max_len = current_sum

    if max_len == n:
        return

    for i in range(index, len(arr)):
        _solve(arr, current_sum + arr[i], i + 1, n)


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        mas = [int(el) for el in line.split()]
        n = mas[0]
        tracks = mas[2:]
        
        result = solve(n, tracks)

        print(f"sum:{result}")


if __name__ == "__main__":
    main()