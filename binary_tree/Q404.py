#%%
# the idea is to use recurison, the total sum of left nodes 
# = sum of left nodes in left subtree and sum of left nodes in right subtree
# we judge whether a node is a left node based on its parent node
#%%
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#%%
class Solution:
    def sumOfLeftLeaves(self, root: [TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        left_sum = self.sumOfLeftLeaves(root.left)
        right_sum = self.sumOfLeftLeaves(root.right)
        if root.left and not root.left.left and not root.left.right:
            left_sum = root.left.val
        return left_sum + right_sum
#%%
Node1 = TreeNode(1)
Node2 = TreeNode(2)
Node3 = TreeNode(3)
Node4 = TreeNode(4)
Node5 = TreeNode(5)

Node1.left = Node2
Node1.right = Node3
Node2.left = Node4
Node2.right = Node5

#%%
S = Solution()
print(S.sumOfLeftLeaves(Node1))