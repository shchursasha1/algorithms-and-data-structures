def first_binary_search(arr, el):
    l = 0
    r = len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < el:
            l = mid + 1
        else:
            r = mid
    return l

def last_binary_search(arr, el):
    l = 0
    r = len(arr)
    while l < r:
        m = l + (r - l) // 2
        if arr[m] <= el:
            l = m + 1
        else:
            r = m
    return l - 1

with open("input.txt") as file:
    temp_1 = file.readline()
    arr = [int(el) for el in file.readline().split()]
    temp_2 = file.readline()
    needed_species = [int(el) for el in file.readline().split()]
    for el in needed_species:
        start = first_binary_search(arr, el)
        end = last_binary_search(arr, el)
        print(end - start + 1)