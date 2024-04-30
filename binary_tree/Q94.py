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

#%%
# use iteraction to solve the problem 
# the idea is keep put left child to the stack until there is no left child
# then pop from the stack save the result and put the right children in stack

#%%
class Solution2:
    def inorderTraversal(self, root) -> list[int]:
        if root == None:
            return []
        stack = []
        result = []
        cur = root
        while cur or len(stack):
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result
    
#%%