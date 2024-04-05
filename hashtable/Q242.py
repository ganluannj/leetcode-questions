#%%
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        records = [0] * 26
        for letter in s:
            records[ord(letter)-ord('a')] += 1
        for letter in t:
            records[ord(letter)-ord('a')] -= 1
        for count in records:
            if count != 0:
                return False
        return True

#%%
s = 'anagram'
t = 'nagaram'
S = Solution()
print(S.isAnagram(s, t))