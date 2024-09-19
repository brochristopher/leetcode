class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # start at the first index value
        # compare it to the next index

        firstNum = ''
        secondNum = ''

        for outerindex, outervalue in enumerate(nums):
            firstNum = outervalue
            for innerindex, innervalue in enumerate(nums):
                if outerindex != innerindex:
                    secondNum = innervalue
                    if firstNum + secondNum == target:
                        return(outerindex,innerindex)
