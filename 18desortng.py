import sys
def solve():
    input= sys.stdin.readline
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        gap = abs(a[0]-a[1])

        
        if a != sorted(a):
            print(0)
        else:
            for i in range(2 , n):
                    gap = min(gap, (a[i] -a[i-1]))
            print((gap//2 )+1 )
           
        
solve()