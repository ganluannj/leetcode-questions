#%%

# =============================================================================
# sliding window
# initialize left and right index of the window with 0
# move the right to the right and calculate the sum of elements between
# left and right index (included), stop moving with the sum is over the target
# 
# move left index to right until one more move the sum is less than the target
# repeat this proces until the right index reaches the end of the list
# =============================================================================
class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        moving_sum = 0
        result = float ('inf')
        for right in range(0, len(nums)):
            moving_sum += nums[right]
            while moving_sum>=target:
                subL = right - left + 1
                result = min(result, subL)
                moving_sum -= nums[left]
                left += 1
        if result < float('inf'):
            return result
        else:
            return 0
#%%


                    
                    
                
            