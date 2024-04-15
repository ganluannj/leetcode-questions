#%%
# to compare whether a tree is symmetric, we only need to check whether
# the subtrees L and R are symmetric or not 
# for two subtress to be symmetric, the root should be the same
# the left tree of L should be symmetric to the right tree of R
# the right tree of L should be symmetric to the left tree of R
#%%
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

#%%
class Solution:
    def isSymmetric(self, root: [TreeNode]) -> bool:
        if not root:
            return True
        return self.subTreeSymm(root.left, root.right)
    
    def subTreeSymm(self, left, right):
        if left is None and right is not None:
            return False
        if left is not None and right is None:
            return False
        if left is None and right is None:
            return True
        if left.val != right.val:
            return False
        l_left_symm = self.subTreeSymm(left.left, right.right)
        l_right_symm = self.subTreeSymm(left.right, right.left)
        return l_left_symm and l_right_symm

#%%
