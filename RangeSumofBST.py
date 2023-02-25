# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if R > node.val:
                    dfs(node.right)
        self.ans = 0
        dfs(root)
        return self.ans
# Runtime: 224 ms, faster than 82.22% of Python3 online submissions for Range Sum of BST.
# Memory Usage: 21.9 MB, less than 7.92% of Python3 online submissions for Range Sum of BST.