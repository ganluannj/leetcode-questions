#%%# the first idea is to use DP, and we have a list to store the largest product # M[j] is the largets product of integer j# set M[0] be 0, and M[1] be 1# base case M[2] =1# induction rule, for M[j], we cut the rope from the left to right # and calcuate the max product for each cut and then take the maximum of all# these products#  左大段 + 右大段 思想#%%class Solution:    def integerBreak(self, n: int) -> int:        m = [0 for _ in range(n+1)]        m[1] = 1        m[2] = 1        for i in range(2, n+1):            cur_max = 1            for j in range(1, i):                left_max = max(j, m[j])                right_max = max(i-j, m[i-j])                prod = left_max * right_max                if prod > cur_max:                    cur_max = prod            m[i] = cur_max        return m[n]#%%S = Solution()n=10print(S.integerBreak(n))#%%# the second idea is also use DP with the same setting as above# the only thing change is the induction rule, # for M[j]here we look at  the lenght of the right most part # and its length could be from 1 to j-1class Solution2:    def integerBreak(self, n: int) -> int:        m = [0 for _ in range(n+1)]        m[1] = 1        m[2] = 1        for i in range(2, n+1):            cur_max = 1            for j in range(1, i):                left_max = max(i-j, m[i-j])                prod = left_max * j                if prod > cur_max:                    cur_max = prod            m[i] = cur_max        return m[n]#%%S = Solution2()n=10print(S.integerBreak(n))