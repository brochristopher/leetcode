class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # start at the first index value
        # compare it to the next index

        firstNum = ''
        secondNum = ''

# Perhaps it would be better to work from both sides of the list at the same time, working toward the middle.
        for outerindex, outervalue in enumerate(nums):
            if outervalue < target:
                firstNum = outervalue
                for innerindex, innervalue in enumerate(nums):
                  if innervalue < target and outerindex != innerindex:
                    secondNum = innervalue
                    if firstNum + secondNum == target:
                        return(outerindex,innerindex)
