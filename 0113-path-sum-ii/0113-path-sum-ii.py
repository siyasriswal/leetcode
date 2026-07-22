class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        ans = []

        def dfs(node, target, path):
            if node is None:
                return

            path.append(node.val)

            if node.left is None and node.right is None and target == node.val:
                ans.append(path[:])   # copy the current path
            else:
                dfs(node.left, target - node.val, path)
                dfs(node.right, target - node.val, path)

            path.pop()   # backtrack

        dfs(root, targetSum, [])

        return ans