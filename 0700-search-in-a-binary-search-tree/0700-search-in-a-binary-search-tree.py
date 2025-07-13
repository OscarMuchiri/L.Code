# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Start searching from the root of the tree
        curr = root

        # Traverse the tree until we find the value or reach a null node
        while curr and curr.val != val:
            if val < curr.val:
                # If the value to find is smaller, go to the left subtree
                curr = curr.left
            else:
                # If the value to find is larger, go to the right subtree
                curr = curr.right

        # Return the node if found, or None if not found
        return curr
