#%%
# use DP, m to store the number of jumps
# m[j] presents the smallest of jumps needed to reach the last index from index i
# m[n-1]= 0
# m[j] = min(m[i]) + 1 for i > j and i <= j + input[j]
#%%

class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        m = [0 for _ in range(n)]
        indices = [n-k for k in range(2, n+1)]
        for j in indices:
            cur_min = n
            for i in range(j+1, min(j+nums[j]+1, n)):
                steps = m[i] + 1
                if steps < cur_min:
                    cur_min = steps
            m[j] = cur_min
        return m[0]
    
#%%
nums = [2,3,1,1,4]
S = Solution()
print(S.jump(nums))
    
    