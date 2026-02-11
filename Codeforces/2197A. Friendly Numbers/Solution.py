def solve(n):

    if n%9 != 0:
        return 0
    
    for y in range(n+1, n+200):
        dy = sum(int(char) for char in str(y))
        if y - dy == n:
            return 10
        
    return 0

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))