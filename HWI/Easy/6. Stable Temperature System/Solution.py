n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

narr = arr[:]

for i in range(1, n):
    narr[i] = min(narr[i], narr[i-1] + 1)

for i in range(n-2, -1, -1):
    narr[i] = min(narr[i], narr[i+1] + 1)

ops = 0
for i in range(n):
    ops += abs(arr[i]-narr[i])

print(ops)