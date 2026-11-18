import sys
def solve():
    
    input = sys.stdin.readline
    t= int(input())
    for _ in range(t):
        seen={}
        n = int(input())
        a = list(map(int,input().split()))
        for i in range(n):
            seen[a[i]] = seen.get(a[i] , 0 )+1 

        if len(seen) == 1:
            print("Yes")
        elif len(seen) == 2:
            counts = list(seen.values())
            if abs(counts[0] - counts[1]) <=1:
                print("Yes")
            else:
                print("No")
        else:
            print("No") 
solve()

