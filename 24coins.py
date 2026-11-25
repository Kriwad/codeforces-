import sys 
def solve():
    input= sys.stdin.readline
    t = int(input())
    for _ in range(t):
        x ,k = list(map(int , input().split()))
        if x % 2 == 0 :
            print("YES")
        elif k%2 != 0 and x >= k:
            print("YES")
        else:
            print("NO")

solve()
