#Soluciones por Pablo Moreno Moreu, Arnau Neches Vila, Carlos Fernandez-LLebrez Acedo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False
        if p.val != q.val:
            return False
        if p.val == q.val:
            return True and self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)