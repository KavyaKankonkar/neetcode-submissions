# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None :
            return False
        if self.isSameTree(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        # elif root is not None and subRoot is not None:
        #     if root.val==subRoot.val:
        #         if self.isSubtree(root.left,subRoot.left) and self.isSubtree(root.right,subRoot.right):
        #             return True
        #         else:
        #             if (self.isSubtree(root.left,subRoot)) :
        #                 return True
        #             else:
        #                 return self.isSubtree(root.right,subRoot) 
        #     else:
        #         if (self.isSubtree(root.left,subRoot)) :
        #             return True
        #         else:
        #             return self.isSubtree(root.right,subRoot) 
        #     else:
        #         return False
    def isSameTree(self,p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            if p.val==q.val:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False

