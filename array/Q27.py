# =============================================================================
# 1st solution
# go through the list and found the element equals to val
# once found it, remove all the elements after it one poisition ahead
# =============================================================================
# 
# nums = [2,3,4,5,2]
# val = 2
# 1st step: i=0, size = 5, nums[i]==val
#   nums = [3,4,5,2,_], size = 4, i = 0
# 2nd step i = 0,, size = 4, nums[i]!=val -> i = 1
# 3rd step nums[i]!=val, -> i =2
# 4th step: nums[i]!=val, -> i=3
# 5th step: nums[i]==val -> i=3, size=3, nums =[3,4,5,2,_]
# =============================================================================
# =============================================================================
#%%
class Solution ():
    def replace(self, nums, val):
        i, size = 0, len(nums)
        while i<size:
            if nums[i]==val:
                for j in range(i+1, size):
                    nums[j-1] = nums[j]
                i -=1
                size -=1
            i +=1
        return size
    
#%%
S = Solution()
nums = [2,3,4,5,2]
print(S.replace(nums, 2))
print(nums)
            
#%%
# =============================================================================
# two index, fast and slow index
# use the fast index to go through the list
# elements before and on the slow index are elements not equal to val
# slow +1 is the size we need to return 
# =============================================================================
class Solution2:
    def replace(self, nums, val):
        slow, fast = 0,0
        while fast < len(nums):
            if nums[fast]==val:
                nums[slow]=nums[fast]
                slow += 1
            fast += 1
        return slow
#%%
S = Solution2()
nums = [2,3,4,5,2]
print(S.replace(nums, 2))
print(nums)
        