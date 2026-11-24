import sys

def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n , k, x = map(int , input().split()) 
        ans = []
    
        if x != 1:
            for i in range(n):
                ans.append(1)
            print("YES")
            print(len(ans))
            print(" ".join(map(str , ans)))

        elif x == 1 and k >= 2 and n % 2 == 0 :
            for i in range(int(n/2)):
                ans.append(2)
            print("YES")
            print(len(ans))
            print(" ".join(map(str, ans)))

        elif x == 1 and k >= 3 and n >= 3:
            ans.append(3)
            for i in range((n-3)//2):
                ans.append(2)
            print("YES")
            print(len(ans))
            print(" ".join(map(str,ans)))
        else:
            print("NO")


solve()
            

                
