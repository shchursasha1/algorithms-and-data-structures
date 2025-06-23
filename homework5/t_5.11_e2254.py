import sys

def solve():
    try:
        r_str, l_str, b_str = sys.stdin.readline().split()
        r = int(r_str)
        b = int(b_str)
    except (IOError, ValueError):
        return

    if r == 0:
        print(0)
        return

    x = [0] * r
    for i in range(r):
        x[i] = int(sys.stdin.readline())

    prefix_sums = [0] * (r + 1)
    for i in range(r):
        prefix_sums[i + 1] = prefix_sums[i] + x[i]

    low = 1
    high = r
    ans = 0

    while low <= high:
        k = (low + high) // 2
        if k == 0:
            break

        is_possible = False
        
        i = 0
        while i <= r - k:
            median_idx_in_window = (k - 1) // 2
            median_abs_idx = i + median_idx_in_window
            median_val = x[median_abs_idx]
            
            count_left = median_idx_in_window + 1
            sum_left = prefix_sums[median_abs_idx + 1] - prefix_sums[i]
            cost_left = median_val * count_left - sum_left
            
            count_right = k - count_left
            sum_right = prefix_sums[i + k] - prefix_sums[median_abs_idx + 1]
            cost_right = sum_right - median_val * count_right
            
            total_cost = cost_left + cost_right

            if total_cost <= b:
                is_possible = True
                break
            i += 1

        if is_possible:
            ans = k
            low = k + 1
        else:
            high = k - 1

    print(ans)


solve()