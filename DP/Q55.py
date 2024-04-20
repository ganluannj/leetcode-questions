#%%
# we use dynamic programming, we use a list to store whether we can reach
# the last index from current index
# we start from the index n-1 (base case)
# for m[j] it is true, if there is at least one index i such that m[i] is true
# and i > j and i <=j + input[j]
#%%

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        m = [False for _ in range(len(nums))]
        n = len(nums)
        m[n-1] = True
        indices = [n-k for k in range(2, n+1)]
        for j in indices:
            bo = False
            max_jumps = nums[j]
            for i in range(j+1, min(n, j+max_jumps+1)):
                if m[i] == True:
                    bo = True
                    break
            m[j] = bo
        return m[0]
    
#%%

nums = [2,3,1,1,4]
S = Solution()
print(S.canJump(nums))
        
   