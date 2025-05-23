class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        L = 0  # Left pointer
        R = n - 1  # Right pointer
        
        while L < R:
            # Skip all the non-alphanumeric characters from the left
            if not s[L].isalnum():
                L += 1
                continue  # Skips the rest of the loop and move to the next character
            
            # Skip non-alphanumeric characters from the right
            if not s[R].isalnum():
                R -= 1
                continue  # Skips the rest of the loop and move to the next character
            
            # Now Compare the characters in lowercase
            if s[L].lower() != s[R].lower():
                return False  # If mismatch found, it's not a palindrome
            
            # Move both pointers toward the center
            L += 1
            R -= 1
        
        return True  # If all matching characters, it's a palindrome



            
