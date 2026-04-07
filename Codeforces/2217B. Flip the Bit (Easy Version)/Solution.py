t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    p = int(input().split()[0]) 

    flip1 = 0
    for i in range(0, p):
        if (a[i]+flip1)%2 != a[p-1]:
            flip1 += 1

    flip2 = 0
    for i in range(n-1, p-2, -1):
        if (a[i]+flip2)%2 != a[p-1]:
            flip2 += 1

    print(max(flip1, flip2))