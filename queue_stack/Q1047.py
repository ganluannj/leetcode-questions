#%%
# the idea is to put lettres in stack and for every new letter check 
# whether it is the same as the last letter, if it is the same then 
# remove the last letter in the stack, otherwise put the new letter
# in the stack

#%%
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for l in s:
            if (not stack) or (stack[-1] != l):
                stack.append(l)
            else:
                stack.pop()
        return ''.join(stack)

#%%
S = Solution()
s = "abbaca"
print(S.removeDuplicates(s))                
