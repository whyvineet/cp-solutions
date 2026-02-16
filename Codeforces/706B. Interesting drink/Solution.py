from bisect import bisect_right

def solve(x, m):
    
    return bisect_right(x, m)

if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    q = int(input())
    for _ in range(q):
        m = int(input())
        print(solve(x, m))