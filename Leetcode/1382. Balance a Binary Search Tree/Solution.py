# https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        a = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            a.append(root)
            inorder(root.right)
        inorder(root)

        def BST(l, r):
            if l > r:
                return None
            mid = (l+r)//2
            a[mid].left = BST(l, mid - 1)
            a[mid].right = BST(mid + 1, r)
            return a[mid]
        return BST(0, len(a)-1)