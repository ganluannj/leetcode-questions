#%%
# {[]}()
# the idea is if we see a left parenthesis, we push to stack
# when we see a right parenthesis, we pop the stack 
# the poped parenthesis should be paired with the right parenthesis
#%%
class Solution:
    def isValid(self, s: str) -> bool:
        if s is None:
            return True
        if len(s) == 0:
            return True
        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                else:
                    judgement = self.check_pair(stack.pop(), s[i])
                    if judgement is False:
                        return False
        if len(stack) > 0:
            return False
        return True
    
    def check_pair(self, left, right):
        if right == '}':
            if left != '{':
                return False
        if right == ')':
            if left != '(':
                return False
        if right == ']':
            if left != '[':
                return False

#%%
class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()
        
        return True if not stack else False
#%%
S = Solution()
s = '(]'
print(S.isValid(s))
        