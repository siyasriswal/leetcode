# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root):

        def dfs(node):

            if node is None:
                return 0

            total = 0

            if node.left:

                if node.left.left is None and node.left.right is None:
                    total += node.left.val

            total += dfs(node.left)
            total += dfs(node.right)

            return total

        return dfs(root)