import sys 
def solve():
    input =sys.stdin.readline
    t= int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int , input().split()))
        b =[]
        for i in range( n):
            b.append(n+1-a[i])


        print(" ".join(map(str , b)))

solve()