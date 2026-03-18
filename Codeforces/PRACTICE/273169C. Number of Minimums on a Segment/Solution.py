import sys
sys.setrecursionlimit(10**9)

n, q = map(int, input().split())
arr = list(map(int, input().split()))

tree = [(float('inf'), 0)] * (4*n)

def combine(pair1, pair2):

    if pair1[0] < pair2[0]:
        return pair1
    if pair2[0] < pair1[0]:
        return pair2
    
    return (pair1[0], pair1[1] + pair2[1])

def build(idx, l, r):

    if l == r:
        tree[idx] = (arr[l], 1)
        return
    
    m = (l + r) // 2
    build(2*idx+1, l, m)
    build(2*idx+2, m+1, r)

    tree[idx] = combine(tree[2*idx+1], tree[2*idx+2])

build(0, 0, n-1)

def query(idx, l, r, ql, qr):

    if ql > r or qr < l:
        return (float('inf'), 0)
    
    if ql <= l and r <= qr:
        return tree[idx]
    
    m = (l + r) // 2
    left = query(2*idx+1, l, m, ql, qr)
    right = query(2*idx+2, m+1, r, ql, qr)

    return combine(left, right)

def update(idx, l, r, i, nv):

    if l == r:
        tree[idx] = (nv, 1)
        return

    m = (l + r) // 2
    if i <= m:
        update(2*idx+1, l, m, i, nv)
    else:
        update(2*idx+2, m+1, r, i, nv)
    
    tree[idx] = combine(tree[2*idx+1], tree[2*idx+2])

for _ in range(q):
    k, a, b = map(int, input().split())
    if k == 1:
        update(0, 0, n-1, a, b)
    if k == 2:
        res = query(0, 0, n-1, a, b-1)
        print(*res)
