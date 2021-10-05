class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    result: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:

        def dfs(node: TreeNode):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if node.left and node.val == node.left.val:  # 같다면 계속 1을 추가해준다 (누적거리계산)
                left += 1
            else:
                left = 0  # 같지 않다면 0으로 리셋시켜버린다
            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0
            self.right = max(self.result, left + right)
            return left + right

        dfs(root)
        return  self.result
