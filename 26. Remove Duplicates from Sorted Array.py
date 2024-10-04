class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueNums = []

        for index, value in enumerate(nums):
            if value not in uniqueNums:
                uniqueNums.append(value)   
        
        nums[:] = uniqueNums
