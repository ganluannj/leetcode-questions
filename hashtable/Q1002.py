#%%
# the idea is to use a hashtable to store the occurrence of each of these
# 26 letters in each word
# then calculate the minimum of occurrences across all words
#%%
class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        if len(words)==0:
            return []
        hash0 = [0] * 26
        for l in words[0]:
            hash0[ord(l)-ord('a')] += 1
        for i in range(1, len(words)):
            hashword = [0] * 26
            for l in words[i]:
                hashword[ord(l)-ord('a')] += 1
            for i in range(26):
                hash0[i] = min(hash0[i], hashword[i])
        result = []
        for i in range(26):
            while hash0[i]>0:
                result.append(chr(i + ord('a')))
                hash0[i] -= 1
        return result

#%%
S = Solution()
words = ["bella","label","roller"]
print(S.commonChars(words))
                
