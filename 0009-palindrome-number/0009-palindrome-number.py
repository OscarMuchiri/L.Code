class Solution:
    def isPalindrome(self, x: int) -> bool: #212, 312
        if x < 0 or (x % 10 == 0 and x != 0): #Negatives are non palindromes
            return False
        
        reverted_number = 0

        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10

            x = x // 10

        return x == reverted_number or x == reverted_number // 10
        

