import sys

def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        total= 0 
        for i in range(10):
            row =list(input().strip())
            if 'X'in row:
                for j in range(10):
                    if row[j] == "X":
                        steps = min(i , 9-i , 9-j  , j )+1
                        total += steps
                        
                

        print(total)
solve() 