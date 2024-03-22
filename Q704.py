#%%
class Solution:
    def search(self, nums, target) -> int:
        left, right = 0, len(nums) -1 
        while left <=right:
            mid = left + (right - left)//2
            if nums[mid]==target:
                return mid
            elif target < nums[mid]:
                right = mid -1 # remember to -1, otherwise it might get stuck in a dead cycle
            else:
                left = mid +1
        return -1

#%%

S = Solution()
print(S.search([0,1,2,3],5))