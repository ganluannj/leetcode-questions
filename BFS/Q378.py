#%%
# high level idea is to use a min-heap to store elements 
# pop k times to find the k-th smallest element
# after pop each element, we generate two more element 
# one to its left and one to its bottom and put them into the heap  
# use a matrix of boolen of the same size of the original matrix to 
# indicate whether the element has been visited
#%%
# time complexity 
# since we need to pop from a heap for at most k times
# and insert at most 2k times
# the heap length is at most 2k
# time complexity is klog(k)
#%%
# space complexity is Q(n**2)
#%%
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        from queue import PriorityQueue
        n = len(matrix)
        ind_mat = [[1]*n for _ in range(n)]
        Q = PriorityQueue()
        Q.put((matrix[0][0], 0,0))
        ind_mat[0][0] = 0
        for _ in range(k):
            # first get the smallest element frmo the Q
            cur_smallest = Q.get()
            i , j = cur_smallest[1], cur_smallest[2]
            if i < n-1 and ind_mat[i+1][j]: # we can move one row below
                Q.put((matrix[i+1][j], i+1, j))
                ind_mat[i+1][j]= 0
            if j < n-1 and ind_mat[i][j+1]: # we can move one column right
                Q.put((matrix[i][j+1], i, j+1))
                ind_mat[i][j+1] = 0
        return cur_smallest[0]
            
            
#%%
matrix = [[1,5,9],[10,11,13],[12,13,15]]        
k = 8
S = Solution()
print(S.kthSmallest(matrix, k))