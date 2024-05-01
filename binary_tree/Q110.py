#%%
# to check whether a binary tree is a balanced binary tree we only need to check
# 1. whether the height difference of its left subtree and right subtree are within 1
# 2. whether its left subtree and its right subtree are also balanced binary tree

#%%
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        height_diff = abs(left_height - right_height)
        return height_diff <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)   
    
    def height(self, root) -> int:
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))