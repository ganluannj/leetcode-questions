#%%
# the idea is to use recursion 
# base case: len(L) = 0 -> return None; len(L) = 1 -> TreeNode(L[0])
# the recursion function returns the root of the tree based on in_L and post_L
# in current step, we find the root from the last element of post_L,
# then identify the left nodes and right nodes from both List
# apply recursion on both left nodes and right nodes and apply
# the result to left and right of the root

#%%
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#%%
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> [TreeNode]:
        if not inorder or len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root_value = postorder[-1]
        root = TreeNode(postorder[-1])
        index = self.get_index(inorder, root_value)
        inorder_left = inorder[0:index].copy()
        inorder_right = inorder[(index+1):].copy()
        postorder_left = postorder[0:len(inorder_left)].copy()
        postorder_right = postorder[len(inorder_left):-1].copy()
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)
        return root
    def get_index(self, L, num):
        for i in range(len(L)):
            if L[i] == num:
                return i
            