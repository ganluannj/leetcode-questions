#%%
# use the same method as the binary tree level order traversal 
# just reverse the final result
#%%
#%%
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        from collections import deqeue
        if not root:
            return []
        result =[]
        Q = deqeue()
        Q.append(root)
        while Q:
            cur_level = []
            for _ in range(len(Q)):
                cur_node = Q.popleft()
                cur_level.append(cur_node.val)
                if cur_node.left:
                    Q.append(cur_node.left)
                if cur_node.right:
                    Q.append(cur_node.right)
            result.append(cur_level)
        return result[::-1]