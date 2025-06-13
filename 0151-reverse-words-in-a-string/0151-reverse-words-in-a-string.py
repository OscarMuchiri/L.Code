class Solution:
    def reverseWords(self, s: str) -> str:
        #split converts to a list of words
        #reversed reverses the list
        # " ".join reverts it back to a string 
        return " ".join(reversed(s.split()))