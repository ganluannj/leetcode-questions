#%%
# =============================================================================
# use two indices, one starting from left and one startign from right
# the largest square number is from the two ends
# and going from the two ends to the middle, the square number is getting 
# smaller
# =============================================================================
#%%
class Solution:
    def sortedSquares(self, nums):
        squares = [float('inf')]*len(nums)
        left, right, i = 0, len(nums) - 1, len(nums) - 1
        while left <= right:
            left_square = nums[left]**2
            right_square = nums[right]**2
            if left_square >= right_square:
                squares[i]=left_square
                left += 1
            else:
                squares[i]=right_square
                right -=1
            i-=1
        return squares

#%%
nums = [-4,-1,0,3,10]
S = Solution()
print(S.sortedSquares(nums))

#%%
nums = [1]
S = Solution()
print(S.sortedSquares(nums))