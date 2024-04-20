#%%
# use DP, use a vector m to represent the largest sum of subarray
# for each index
# base case: m[0] = input[0]
# induction rule m[j] represents the the largetes sum of subarray from 0-th 
# index to j-th index, must include the j-th element
# m[j] = m[j-1] + input[j] if m[j-1] is positive
# otherwise m[j] = input[j]
#%%

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        m = [0 for _ in range(n)]
        m[0] = nums[0]
        cur_max = m[0]
        for i in range(1, n):
            if m[i-1] > 0:
                m[i] = m[i-1] + nums[i]
            else:
                m[i] = nums[i]
            if m[i] > cur_max:
                cur_max = m[i]
        return cur_max
    
#%%
nums = [-2,1,-3,4,-1,2,1,-5,4]
S = Solution()
print(S.maxSubArray(nums))