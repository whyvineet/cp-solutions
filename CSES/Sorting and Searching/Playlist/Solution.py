n = int(input())
songs = list(map(int, input().split()))

result = 0
mpp = set()

i = 0
for j in range(n):
    while songs[j] in mpp:
        mpp.remove(songs[i])
        i += 1
    mpp.add(songs[j])
    result = max(result, j-i+1)

print(result)