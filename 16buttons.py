import sys

def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        b = list(map(int, input().split()))
        if b[2]% 2 ==1:
            if b[0] >= b[1]:
                print("First")
            else:
                print('Second')
        else:
            if b[0] > b[1]:
                print("First")
            else:
                print("Second")

solve()
        