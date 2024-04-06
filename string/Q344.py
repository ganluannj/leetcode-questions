#%%
# reverseString the idea is to swap the letters that are symmetric 
# wrt the middle of the string 
# use two index, one at the begining and one at the end 
# swap letters of these two index
# then move the left index one position to right and 
# right index one position to left
# swap letters of these two index
# continue this process until right index < left index

#%%
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if s is None:
            return
        left, right = 0, len(s) - 1
        while left <= right:
            self.swap(s, left, right)
            left += 1
            right -= 1
        return
            
    def swap(self, s, i, j):
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        return

#%%
S = Solution()
s =  ["h","e","l","l","o"]
S.reverseString(s)
print(s)