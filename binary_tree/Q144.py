#%%
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def preorderTraversal(self, root) -> list[int]:
        if root == None:
            return []
        left_list = self.preorderTraversal(root.left)
        right_list = self.preorderTraversal(root.right)
        return [root.val] + left_list + right_list