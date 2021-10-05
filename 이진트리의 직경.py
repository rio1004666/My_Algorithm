
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left=left
        self.right=right


class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode):
        def dfs(node: TreeNode):
            if not node: # 노드가 없는 경우 -1 처리
                return -1
            # 왼쪽 오른쪽의 각 리프노드까지 탐색

            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로 갱신
            self.longest = max(self.longest, left + right + 2)
            # 상태값 (  업데이트하면서 누적해나가면 가장 긴 깊이가 나올것이다. )
            return max(left, right) + 1
        dfs(root)
        return self.longest
