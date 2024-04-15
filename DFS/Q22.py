#%%
'''
in the recursion tree, each level represent one position for left or right
parentheses, thus there are 2*n levels
for each level there are two states, left parenthesis or right parenthesis

'''

#%%
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        string = ''
        result = []
        self.dfs(n, 0, 0, string, result)
        return result
        
    def dfs (self, n, l, r, string, result):
        if l + r == 2*n:
            result.append(string[:])
        if l<n:
            # we can add left parenthesis 
            string += '('
            self.dfs(n, l+1, r, string, result)
            string = string[:-1]
        if r < l:
            # we can add right parenthesis
            string += ')'
            self.dfs(n, l, r+1, string, result)
            string = string[:-1]
        return
#%%
n = 3
S = Solution()
print(S.generateParenthesis(n))