# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue=deque([root])
        res=[]
        while queue:
            level=len(queue)
            li=[]
            for _ in range(level):
                node=queue.popleft()
                li.append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            l=len(li)
            res.append(li[l-1])            
            
        return res
