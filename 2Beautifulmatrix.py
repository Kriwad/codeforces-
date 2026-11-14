for i in range(5):
    row = list(map(int , input().split()))
    for j in range(5):
        if row[j]==1:
            step = abs(i-5//2)+ abs(j-5//2)

print(step)