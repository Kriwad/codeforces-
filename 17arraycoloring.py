import sys
def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        a= list(map(int , input().split()))

        if sum(a)%2 ==1 :
            print("No")
        else:
            print("Yes")

solve()