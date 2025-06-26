class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort potions to allow binary search
        potions.sort()
        res = []

        # Loop through each spell
        for s in spells:
            # Binary search to find the first potion that makes a successful pair
            l, r = 0, len(potions) - 1
            idx = len(potions)  # Default to no successful pair

            while l <= r:
                m = (l + r) // 2  # Middle index
                # Check if the product of current spell and potion is >= success
                if s * potions[m] >= success:
                    # Move left to find earlier possible success
                    r = m - 1
                    idx = m  # Update index of first successful potion
                else:
                    # Move right to search for stronger potions
                    l = m + 1

            # The number of successful potions = total potions - index of first success
            res.append(len(potions) - idx)

        return res


        
