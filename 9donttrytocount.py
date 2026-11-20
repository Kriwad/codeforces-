
import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    
    for _ in range(t):
        step =0 
        found = False
        n , m =  map(int,input().split())
        x = str(input().strip())
        s = str(input().strip())
        for i in range(6):
            if s in x:
                print(step)
                found= True
                break
            
            x = x+x
            step +=1 
        if not found:
            print(-1)
        
solve()