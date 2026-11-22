import sys

def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        total= 0 
        for i in range(10):
            row =list(input().strip())
            if 'X'in row:
                for j, ch in enumerate(row):
                    if ch == 'X':
                        total += min(i, 9 - i, j, 9 - j) + 1
        print(total)
solve() 