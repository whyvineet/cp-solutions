def odd_base(x):
    while x%2 == 0:
        x //= 2
    return x

def solve(n, a):
    for i in range(1, n+1):
        if odd_base(i) != odd_base(a[i-1]):
            return "NO"

    return "YES"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(n, a))