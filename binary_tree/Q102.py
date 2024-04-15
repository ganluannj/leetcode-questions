#%%
# the idea is to have a queue to store the node
# pop a node from the queue and save its value 
# then push node's left and right child into queue
# use the size of the queue to indicate the number of nodes in each level
# stop when the queue is empty
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
        return result

#%%

        