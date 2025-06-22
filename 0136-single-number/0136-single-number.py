class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize a variable to hold the result
        # Start with 0 because 0 ^ x = x for any number x
        a = 0

        # Loop through each number in the list comparing to the current a
        for x in nums:
            # XOR the current number with the result
            # Pairs cancel out (e.g., 4 ^ 4 = 0), so only the unique number remains eventually
            a ^= x

        # After the loop, 'a' will hold the number that appeared only once
        return a
