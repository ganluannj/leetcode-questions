#%%
# for the recursion tree, each level represents one position of the list
# for each level, the number of states is the number of elements remaining
# for the questions that each result is the permutation of the original we use 
# SWAP

#%%
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        self.dfs(nums, 0, result)
        return result
        
    def dfs(self, nums, index, result):
        if index == len(nums):
            result.append(nums.copy())
            return
        for i in range(index, len(nums)):
            self.swap(nums, index, i)
            self.dfs(nums, index+1, result)
            self.swap(nums, i, index)
        return
    
    def swap(self, nums, i, j):
        nums[i] , nums[j] = nums[j], nums[i]
        return

#%%
nums = [1,2,3]
S = Solution()
print(S.permute(nums))
        