#%%
# the idea is to check if we split the words into two parts whether
# the left part can be concanate from the dictionary 
# and also the right part is directly from the dictionary
# we use a list to store whether the left parts of the words can be 
# concanated from the dictionary 
# m[j] is a boolen and means whether the 0th letter to j-th letter this
# part can be concanated from the dictionary
#%%
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        m= [False for _ in range(len(s))]
        if s[0] in wordDict:
            m[0] = True
        for i in range(1, len(s)):
            cur = False
            # check whether the  whole part s[0:i+1] is from the 
            # dictionary 
            sub_string = s[0:i+1]
            sub_string_bo = sub_string in wordDict
            cur = cur or sub_string_bo
            
            for j in range(0, i):
                left_bo = m[j]
                right_sub_str = s[j+1, i+1]
                right_bo = right_sub_str in wordDict
                cur = cur or (left_bo and right_bo)
            m[i] = cur
        return m[len(s)-1]

#%%
s = "leetcode"
wordDict = ["leet","code"]
S = Solution()
print(S.wordBreak(s, wordDict))
