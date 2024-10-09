class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        for index, value in enumerate(nums):
            otherNums = nums[:index] + nums[index+1:]
            if value not in otherNums:
                return value
