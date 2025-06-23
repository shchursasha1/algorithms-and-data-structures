import sys

def solve():
    n_str = sys.stdin.readline()
    
    collection = set(sys.stdin.readline().split())
    
    m_str = sys.stdin.readline()

    queries = sys.stdin.readline().split()
    
    for butterfly in queries:
        if butterfly in collection:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")

solve()