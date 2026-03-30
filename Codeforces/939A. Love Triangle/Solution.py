n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    if arr[arr[arr[i]-1]-1] == i+1:
        print("YES")
        break
else:
    print("NO")