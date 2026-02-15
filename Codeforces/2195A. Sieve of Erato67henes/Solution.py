def solve(a):
    for i in a:
        if i == 67:
            return "YES"
    return "NO"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))