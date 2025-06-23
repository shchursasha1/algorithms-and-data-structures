import sys

def generate(n, current_sequence, stack):
    if len(current_sequence) == n:
        if not stack:
            print(current_sequence)
        return

    if (len(current_sequence) + len(stack)) < n:
        generate(n, current_sequence + '(', stack + ['('])
        generate(n, current_sequence + '[', stack + ['['])

    if stack:
        if stack[-1] == '(':
            generate(n, current_sequence + ')', stack[:-1])
        elif stack[-1] == '[':
            generate(n, current_sequence + ']', stack[:-1])


def main():
    try:
        n = int(sys.stdin.readline())
        if n % 2 == 0 and n > 0:
            generate(n, "", [])
    except (IOError, ValueError):
        return

main()