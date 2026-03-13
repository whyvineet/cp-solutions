def solve(l, r, array, remove):

    while l <= r:
        if array[l] == array[r]:
            l += 1
            r -= 1
        elif array[l] == remove:
            l += 1
        elif array[r] == remove:
            r -= 1
        else:
            return False
        
    return True

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    l, r = 0, n-1
    used = False
    while l <= r:

        if arr[l] == arr[r]:
            l += 1
            r -= 1
        else:
            break
    
    if l > r:
        print("YES")
    else:
        left = solve(l+1, r, arr, arr[l])
        right = solve(l, r-1, arr, arr[r])

        if left or right:
            print("YES")
        else:
            print("NO")