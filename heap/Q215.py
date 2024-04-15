#%%
# the idea is to keep a min heap with length of k 
# we push the first k elements in the arry to this heap 
# for the elements after that, we check wheather it is larger than the 
# smallest value heap, if yes, put it in heap
# otherwise do nothing
# in this way we store the k largest elements in heap
# and the smallest one of these k largeest elements 
# is the k-th largest element in the array 

#%%
# since for each element we need to perform a insert action into 
# the heap with size of k, thus the time complexity is O(nlogk)
# space complexity is O(k)

#%%
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        from queue import PriorityQueue
        Q = PriorityQueue()
        for i in range(k):
            Q.put(nums[i])
        for i in range(k, len(nums)):
            cur_min = Q.queue[0]
            if nums[i] > cur_min:
                Q.get()
                Q.put(nums[i])
        return Q.queue[0]
    

#%%
nums = [1,3,2,5,4,6,7]
k = 2   
S = Solution()
print(S.findKthLargest(nums, k))