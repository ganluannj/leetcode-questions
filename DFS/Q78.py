#%%
# for example for the set ['a', 'b', 'c']
# have the recursion tree
# each level represent each letter in the list
# and each letter has two states, being in the final subset or 
# not in the final subset
#                           []
#                         'a'/  \''
#                         ['a']      []
#                      'b'/   \''   'b'/  \''
#                    ['a', 'b'] ['a']
#                    'c'/   \''
#            ['a','b','c'] ['a', 'b']
#%%
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if nums is None:
            return []
        if len(nums) == 0:
            return [[]]
        result = []
        cur_subset = []
        self.dfs(nums, 0, cur_subset, result)
        return result
        
    def dfs (self, nums, index, subset, result):
        if index == len(nums):
            result.append(subset.copy())
            return 
        # include current letter
        subset.append(nums[index])
        # call dfs of next level
        self.dfs(nums, index+1, subset, result)
        subset.pop()
        # does not include current letter
        self.dfs(nums, index+1, subset, result)
        return
#%%
nums = [1,2,3]
S = Solution()
print(S.subsets(nums))