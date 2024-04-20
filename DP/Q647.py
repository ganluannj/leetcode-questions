#%%
# to use DP
# We use a list to store the longest ascending subarry so far M
# M[i] represents the starting from the left most element 
# the longest ascending subarray including input[i]
# base case M[0] = 1
# induction rule: M[i] = M[i-1] + 1 if M[i] > M[i-1]
# else M[i] = 1

#%%
class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        M = [0 for _ in range(len(nums))]
        M[0] = 1
        max_length = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                M[i] = M[i-1] + 1
                if M[i] > max_length:
                    max_length = M[i]
            else:
                M[i] = 1
        return max_length

#%%
nums = [1,3,5,4,7]
S = Solution()
S.findLengthOfLCIS(nums)
        