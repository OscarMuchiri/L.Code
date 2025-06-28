# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If root is None, return None (base case)
        if not root:
            return None

        # If the current node is either p or q, return it
        if root == p or root == q:
            return root

        # Recursively search for p and q in the left and right subtrees
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # If both sides returned a node, current node is the LCA
        if l and r:
            return root
        else:
            # If only one side is non-null, return it
            return l or r


    
        