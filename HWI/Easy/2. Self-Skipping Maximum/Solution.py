n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

# Recursion
"""
def solve(i):
    if i >= n:
        return 0
    
    pck = arr[i] + solve(i+arr[i]+1)
    npk = solve(i+1)

    return max(pck, npk)

print(solve(0))
"""

# Memoization
"""
dp = [-1]*n

def solve(i):
    if i >= n:
        return 0
    
    if dp[i] != -1:
        return dp[i]
    
    pck = arr[i] + solve(i+arr[i]+1)
    npk = solve(i+1)

    dp[i] = max(pck, npk)
    return dp[i]

print(solve(0))
"""

# Tablulation
dp = [0]*n
dp[n-1] = arr[n-1]
for i in range(n-2, -1, -1):
    nxt = 0
    if i+arr[i]+1 < n:
        nxt = dp[i+arr[i]+1]
    dp[i] = max(arr[i]+nxt, dp[i+1])

print(dp[0])