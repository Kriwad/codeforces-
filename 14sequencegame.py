import sys
def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
       
        n = int(input())
        b = list(map(int, input().split()))
        a = [b[0]]
        for i in range(1 ,len(b)):
            if b[i-1]<= b[i]:
                a.append(b[i])
            else:
                a.append(b[i])
                a.append(b[i])
            

        print(int(len(a)))
        print(" ".join(map(str , a )))
solve()