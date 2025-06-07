class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort() #increasing 

        return nums[len(nums)//2] #Exists at the middle
        
        
        