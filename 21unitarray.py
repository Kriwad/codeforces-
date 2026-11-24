import sys
def solve():
    input = sys.stdin.readline
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        count_p = a.count(1)
        count_n = a.count(-1)
        ans = 0
        while count_n > count_p:
            count_n-=1
            count_p+=1
            ans+=1
         #   print("while",ans) 

        if count_n %2 != 0:
            ans+=1
           
        
        print(ans)

solve()