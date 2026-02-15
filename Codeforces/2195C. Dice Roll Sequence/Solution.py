def solve(n, a):
    
    dp = [0 if a[0]==x else 1 for x in range(1, 7)]

    for i in range(1, n):
        dpp = [float('inf')]*6
        for j in range(1, 7):
            cost = 0 if a[i]==j else 1
            for k in range(1, 7):
                if k != j and j+k != 7:
                    total = dp[k-1] + cost
                    dpp[j-1] = min(dpp[j-1], total)
        dp = dpp

    return min(dp)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(n, a))