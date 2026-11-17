import sys
def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n , x = map(int, input().split())
        a= list(map(int, input().split()))

        ans = a[0]

        for i in range(1 ,n):
            gap = a[i] - a[i-1]
            if gap > ans:
                ans = gap

       
        if (2*(x - a[-1])) > ans:
            ans=  2*(x - a[-1])
        

        print(ans) 
        

solve()