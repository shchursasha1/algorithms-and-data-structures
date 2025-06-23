#---------a---------
#sum_{i=0}^{n} i

def a(n):
    sum = 0                   # O(1)
    for i in range(1 ,n + 1): # O(n)
        sum += i              # O(n)
    return sum                # O(1)

#res: O(n)

#---------b---------
#sum_{i=0}^{n} i^2

def b(n):
    sum = 0                  # O(1)
    for i in range(1,n + 1): # O(n)
        i *= i               # O(n)
        sum += i             # O(n)
    return sum               # O(1)

#res: O(n)

#---------c---------
#sum_{i=0}^{n} a^i

def c(n, a):
    sum = 1                  # O(1)
    temp_a = a               # O(1)
    for i in range(1,n + 1): # O(n)
        temp_a *= a          # O(n)
        sum += temp_a        # O(n)
    return sum               # O(1)

#res: O(n)

#---------d---------
#sum_{i=0}^{n} i^i

def d(n):
    sum = 1                      # O(1)
    for i in range(1,n + 1):     # O(n)
        i **= i                  # O(n^2) = O(1) + O(2) + O(3) + ... + O(n)
        sum += i                 # O(n)
    return sum                   # O(1)

#res: O(n^2)

#---------e---------
#mult_{i=1}^{n} 1 / (1 + i)

def e(n):
    result = 1                # O(1)
    for i in range(1,n + 1):  # O(n)
        result *= 1 / (1 + i) # O(n)
    return result             # O(n)

#res: O(n)

#---------f---------
#mult_{i=1}^{n} 1 / (1 + i!)

def f(n):
    result = 1                     # O(1)
    temp_i = 1                     # O(1)
    for i in range(1,n + 1):       # O(n)
        temp_i *= i                # O(n)
        result *= 1 / (1 + temp_i) # O(n)
    return result                  # O(1)

#res: O(n)

#---------g---------
#mult_{i=1}^{n} a^i / (1 + i!)

def g(n, a):
    result = 1                     # O(1)
    temp_i = 1                     # O(1)
    for i in range(1,n + 1):       # O(n)
        temp_i *= i                # O(n)
        result *= 1 / (1 + temp_i) # O(n)
        a *= a                     # O(n)
    return result                  # O(1)

#res: O(n)

#---------h---------
#mult_{i=1}^{n} 1 / (1 + i^m)

def h(n, m):
    result = 1                # O(1)
    for i in range(1,n + 1):  # O(n)
        i = i ** m            # O(n) * O(m) = O(nm)
        result *= 1 / (1 + i) # O(n)
    return result             # O(1)

#res: O(nm)

#---------i---------
#mult_{i=1}^{n} 1 / (1 + i^i)

def i(n):
    result = 1                # O(1)
    for i in range(1,n + 1):  # O(n)
        i = i ** i            # O(n^2) = O(1) + O(2) + O(3) + ... + O(n)
        result *= 1 / (1 + i) # O(n)
    return result             # O(1)

#res: O(n^2)