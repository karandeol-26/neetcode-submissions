class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       left = 0
       right = len(nums) - 1
       while True:
        if nums[left]+ nums[right] > target:
            right -= 1
            continue
        elif nums[left] + nums[right]< target:
            left += 1
            continue
        else:
            return [left+1, right+1]
        