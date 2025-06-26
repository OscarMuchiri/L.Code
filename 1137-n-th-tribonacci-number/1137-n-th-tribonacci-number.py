class Solution:
    def tribonacci(self, n: int) -> int:
        # Initialize the first three numbers of the Tribonacci sequence
        t = [0, 1, 1]  # T0 = 0, T1 = 1, T2 = 1

        # If n is 0, 1, or 2, return the value directly from the initialized list
        if n < 3:
            return t[n]

        # Loop from 3 to n to compute the nth Tribonacci number
        for i in range(3, n + 1):
            # Shift the window: T(n-3) = T(n-2), T(n-2) = T(n-1), T(n-1) = T(n)
            # The next Tribonacci number is the sum of the previous three
            t[0], t[1], t[2] = t[1], t[2], sum(t)

        # After the loop, t[2] holds the value of Tn
        return t[2]
