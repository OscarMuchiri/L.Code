class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)

        i, j = 0, 0   #pointers 
        result = []  # empty array to append the characters

        while i < m or j < n:
            if i < m:
                result += word1[i]
                i += 1
            
            if j < n:
                result += word2[j]
                j += 1

        return ''.join(result)  #conv array to result string
        

























      


        