from collections import Counter


def solve(n, dam):

    freq = Counter(dam)
    val, count = dam[0], freq[dam[0]]
    for key, value in freq.items():
        if value > count:
            count = value
            val = key

    total = sum(dam)

    rem = n - count
    if count <= rem + 2:
        return total

    return total - (count - (rem + 2)) * val

t = int(input())
for _ in range(t):
    n = int(input())
    dam = list(map(int, input().split()))

    result = solve(n, sorted(dam))
    print(result)