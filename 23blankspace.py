import sys
def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        count = 0 
        ans = 0 
        for i in range(n):
            if a[i] == 0:
                count +=1
                ans = max(count , ans)
            else:
                count = 0 

        print(ans)

solve()