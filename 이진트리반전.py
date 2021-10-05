import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree1(self, root: TreeNode) -> TreeNode:
    if root:
        # 왼쪽 오른쪽 나눠서 노드를 왼쪽 오른쪽을 오른쪽 왼쪽으로 시작하도록 한다.
        # 재귀적으로 나눠서 탐색들어간다.
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    return None


def invertTree2(root: TreeNode) -> TreeNode:
    queue = collections.deque([root])
    while queue:
        # 부모노드부터 하향식 스왑
        # 이 node는 root 트리노드가 참조하는 주소를 같이 참조한다.
        # 그러므로 node가 변경이 되면 root값도 변경된다.
        node = queue.popleft()

        if node:
            node.left, node.right = node.right, node.left  # 반전 즉 뒤바꾼다
            queue.append(node.right)  # 원래 node.left 이다.
            queue.append(node.left)  # 원래 node.right 이다.
    return root



