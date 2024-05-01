#%%
#the idea is that if a tree is a full binary tree, then number of nodes
# will be 2**n - 1, n will be the length of tree, counting from 1
# if not, we can go deep until left or right subtree is a full binary tree

#%%
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = 0
        right_depth = 0
        left = root
        right = root
        while left:
            left_depth += 1
            left = left.left
        while right:
            right_depth += 1
            right = right.right
        if left_depth == right_depth:
            return 2**left_depth - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
