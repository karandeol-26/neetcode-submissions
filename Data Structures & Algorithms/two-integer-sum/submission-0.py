class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i< len(nums)-1:
            for j in range (0,len(nums)):
                if nums[i] + nums[j] == target and i !=j:
                    return [i, j]
            i+=1
        
            