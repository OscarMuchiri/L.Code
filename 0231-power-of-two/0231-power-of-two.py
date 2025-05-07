class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
       #if n== 0 false
       #16 /2 = 8
       #8 /2 = 4
       #4 / 2 = 2
       #2/2 = 1 is a power of two

    #10 / 2 = 5 not a power of 2

        if n == 0:
            return False
        while n % 2 == 0:
            n = n / 2
        return n == 1



        
