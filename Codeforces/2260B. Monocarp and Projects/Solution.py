def helper(left, right, diff):
    total = 0
    curr = left
    while curr <= right:
        q = diff // curr
        if q == 0:
            total += diff * (right - curr + 1)
            break

        last = min(right, diff // q)
        count = last - curr + 1
        total += diff * count - q * (curr + last) * count // 2
        curr = last + 1
    return total

def solve(x, y, k):
    l = x
    r = x + k - 1
    d = y - x

    if d >= 0:
        return helper(d)

    val = -1 * d
    total = (l + r) * k // 2 - helper(val)

    start = (l + val - 1) // val
    end = r // val
    if start <= end:
        count = end - start + 1
        total -= (start + end) * count * val // 2

    return total

t = int(input())
for _ in range(t):
    x, y, k = map(int, input().split())
    result = solve(x, y, k)
    print(result)