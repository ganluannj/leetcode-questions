#%%
# the idea is to use dfs to visit all nodes to the end 
#%%
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#%%
class Solution:
    def binaryTreePaths(self, root: [TreeNode]) -> list[str]:
        if not root:
            return []
        vector = []
        result = []
        self.dfs(root, vector, result)
        return result
    
    def dfs(self, cur, vector, result):
        vector.append(str(cur.val))
        if (cur.left is None) and (cur.right is None):
            result.append('->'.join(vector))
            return
        # traverse left child
        if cur.left:
            self.dfs(cur.left, vector, result)
            vector.pop()
        if cur.right:
            self.dfs(cur.right, vector, result)
            vector.pop()
        return

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
print(S.binaryTreePaths(Node1))