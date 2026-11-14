
def solve():
    test = int(input())
    for _ in range(test):
        n , k = map(int ,input().split())
        a= list(map(int, input().split()))
        if k > 1 or all(a[i] <= a[i+1] for i in range(n-1)):
            print("YES")
        else:
            print("NO")

solve()