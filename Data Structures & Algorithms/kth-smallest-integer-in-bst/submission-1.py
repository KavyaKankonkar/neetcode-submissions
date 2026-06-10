# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        queue=deque([root])
        li=[]
        while queue:
            level_size=len(queue)
            
            for _ in range(level_size):
                node=queue.popleft()
                li.append(node.val)

                if node.left is not None :
                    queue.append(node.left)
                if node.right is not None :
                    queue.append(node.right)
                
        li.sort()
        ind=k-1
        if not li:
            return 0
        else:
            return li[ind]