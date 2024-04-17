#%%
# first we need to sort the list 
# the basic logic is the the same as subset I 
# the only change is that for the letters that are duplicates
# if we do not include the ones in the front we do not include the 
# ones after them
#%%
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        subset = []
        result = []
        self.dfs(nums, 0, subset, result)
        return result
    
    def dfs (self, nums, index, subset, result):
        if index == len(nums):
            result.append(subset.copy())
            return
        
        # include current element 
        subset.append(nums[index])
        self.dfs(nums, index + 1, subset, result)
        subset.pop()
        
        # for the case not include current element
        while (index < len(nums) - 1) and (nums[index] == nums[index + 1]):
            index += 1
        self.dfs(nums, index + 1, subset, result)
        
        return
    
#%%
nums = [3, 1, 2, 2]
S = Solution()
print(S.subsetsWithDup(nums))
                
                           