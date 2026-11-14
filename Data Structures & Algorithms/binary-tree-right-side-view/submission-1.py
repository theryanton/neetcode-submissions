# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: return []

        res = []

        q = deque()
        q.append(root)

        while q:
            qlen = len(q)
            rightMost = None
            for i in range(qlen):
                node = q.popleft()
                rightMost = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if rightMost:
                res.append(rightMost.val)
        return res
