#%%
# use the recursion for the post order traverse 
# end condition: stop when there is no node 
# what should the function return: the function should return the 
# post order traverse of the tree 
# for current level, we should postorder traverse left tree,
# then post traverse right tree, and last current node

#%%
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorderTraversal(self, root) -> list[int]:
        if root == None:
            return []
        left_list = self.postorderTraversal(root.left)
        right_list = self.postorderTraversal(root.right)
        return left_list + right_list + [root.val]
 
#%%
# for iteration, we first get the root, right, left
# reverse the result we get left, right, root
#%%    
class Solution2:
    def postorderTraversal(self, root) -> list[int]:
        if root == None:
            return []
        stack = []
        result = []
        stack.append(root)
        while len(stack):
            cur = stack.pop()
            result.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return result[::-1]

#%%
TN1 = TreeNode(1)
TN2 = TreeNode(2)
TN3 = TreeNode(3)
TN1.right = TN2
TN2.left = TN3

S = Solution()
print(S.postorderTraversal(TN1))