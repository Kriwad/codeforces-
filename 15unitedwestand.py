import sys

def solve():
    t = int(input())
    for _ in range(t):
        b = []
        c = []
        n = int(input())
        a = list(map(int , input().split()))
        m = max(a)
        if min(a) == max(a):
            print(-1)
            
        else:
            for i in a:
                if i == m:
                    c.append(i)
                else:
                    b.append(i)

            print(len(b) , len(c))
            print(" ".join(map(str ,b)))
            print(" ".join(map(str , c)))
solve()