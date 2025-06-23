def cyclic_left_shift(n, bit_size):
    msb = (n >> (bit_size - 1)) & 1
    n = (n << 1) & ((1 << bit_size) - 1)
    n |= msb
    return n


def max_value(n):
    bit_size = n.bit_length()
    max = n
    temp = cyclic_left_shift(n, bit_size)
    while n != temp:
        if max < temp:
            max = temp
        temp = cyclic_left_shift(temp, bit_size)
    return max


n = int(input())
print(max_value(n))