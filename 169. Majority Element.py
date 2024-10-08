class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        countList = {}

        mostFrequentNum = 0

        # If the value isn't present, add it
        for i in nums:
            if i not in countList:
                countList.update({i:1})
        # If the value is there, increment it
            else:
                countList.update({i:countList.get(i)+1})

        # If mostFrequentNum is initialized but hasn't been changed, set it to i
        for i in countList.keys():
            if mostFrequentNum == 0:
                mostFrequentNum = i
        # Otherwise, compare the value at the current key to the value at the key of mostFrequentNum
            elif countList.get(i) > countList.get(mostFrequentNum):
                mostFrequentNum = i
            else:
                continue

        return(mostFrequentNum)
