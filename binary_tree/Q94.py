#%%
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root) -> list[int]:
        if root == None:
            return []
        left_list = self.inorderTraversal(root.left)
        right_list = self.inorderTraversal(root.right)
        return left_list + [root.val] + right_list
