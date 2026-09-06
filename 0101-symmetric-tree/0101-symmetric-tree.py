class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def mirror(left, right):
            if left is None and right is None:
                return True

            if left is None or right is None:
                return False

            return (
                left.val == right.val
                and mirror(left.left, right.right)
                and mirror(left.right, right.left)
            )

        return mirror(root.left, root.right)