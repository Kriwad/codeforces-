import sys
def solve():

    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):

        n = int(input())
        a = list(map(int, input().split()))
        total = sum(a)
        print(-total)

solve()
