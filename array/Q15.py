#%%
# convert the 3 sum problem to 2sum problem 
# first sort the array, use index i to go through the whole list 
# for a certain index i, 
# initiate two indexes, left and right with left = i + 1 and right = N -1
# if nums[l;eft] + nums[right] == - nums[i], then save this tuple
# and move left one position right
# if nums[left] + nums[right] < = -nums[i], move left one position right
# else move right one position left
# for dedup, we move i one position to the right if nums[i] == nums[i-1]
# and when nums[left] + nums[right] == -nums[i], and nums[left] == nums[left -1]
# we move left one position to the right
# why we do not need to dedup right index, because when we find the the target
# tuple, we move left to one position right, we may have two same numbers 
# indexed by left index and recorded twice. 
# however we only move right index when nums[left] + nums[right]  > -nums[i],
# for two numbers that are same and pointed by right index, we will pass them 
# without recording them  
#%%
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        N = len(nums)
        for i in range(N):
            if nums[i]>0:
                continue
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            left, right = i+1, N-1
            while left < right:
                if nums[left] + nums[right] == target:
                    result.append(nums[i], nums[left], nums[right])
                    left = left + 1
                    while nums[left] == nums[left-1]:
                        left = left + 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return result

#%%
