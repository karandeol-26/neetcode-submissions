class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_nums ={}
        for i in nums:
            if i not in dict_nums:
                dict_nums[i] = 1
            else:
                dict_nums[i] += 1

        for num in dict_nums:
            if dict_nums[num] > 1:
                return True
        for num in dict_nums:
            if dict_nums[num] == 1:
                pass
        return False
        

        