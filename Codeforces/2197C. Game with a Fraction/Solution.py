def solve(p, q):

    if q > p and 2*q <= 3*p:
        return "Bob"
    
    return "Alice"
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        p, q = map(int, input().split())
        print(solve(p, q))