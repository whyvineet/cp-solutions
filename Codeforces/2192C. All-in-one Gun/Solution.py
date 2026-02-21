def solve(n, h, k, a):
    total = sum(a)

    cyc = (h-1) // total
    rem = h - (cyc*total)

    suf = [0]*(n+1)
    for i in range(n-1, -1, -1):
        suf[i] = max(suf[i + 1], a[i])

    pre = 0
    mn = float('inf')

    for j in range(1, n+1):
        pre += a[j-1]
        mn = min(mn, a[j-1])

        best = pre
        
        if suf[j] > mn:
            best += suf[j]-mn

        if best >= rem:
            return cyc * (n+k) + j

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, h, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(solve(n, h, k, a))