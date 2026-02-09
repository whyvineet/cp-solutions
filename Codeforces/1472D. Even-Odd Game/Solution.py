def solve(n, a):

    a.sort(reverse=True)

    winner = 0
    for i in range(n):
        if a[i] % 2 ==  0 and i % 2 == 0:
            winner += a[i]
        elif a[i] % 2 == 1 and i % 2 == 1:
            winner -= a[i]

    if winner > 0:
        return "Alice"
    elif winner < 0:
        return "Bob"
    
    return "Tie"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(n, a))