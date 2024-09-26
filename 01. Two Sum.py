class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        firstNum = ''
        secondNum = ''

        for outerindex, outervalue in enumerate(nums):
            firstNum = outervalue
            for innerindex, innervalue in enumerate(nums):
                if outerindex != innerindex:
                    secondNum = innervalue
                    if firstNum + secondNum == target:
                        return(outerindex,innerindex)
