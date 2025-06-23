def can_reach_24(nums):
    if len(nums) == 1:
        return abs(nums[0] - 24) < 1e-6

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue

            a = nums[i]
            b = nums[j]
            remaining = [nums[k] for k in range(len(nums)) if k != i and k != j]

            if can_reach_24(remaining + [a + b]):
                return True
            if can_reach_24(remaining + [a - b]):
                return True
            if can_reach_24(remaining + [b - a]):
                return True
            if can_reach_24(remaining + [a * b]):
                return True
            if b != 0 and can_reach_24(remaining + [a / b]):
                return True
            if a != 0 and can_reach_24(remaining + [b / a]):
                return True

    return False

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        nums = list(map(int, input().split()))
        if can_reach_24(nums):
            print("YES")
        else:
            print("NO")