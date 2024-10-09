class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize a dictionary
        seen = {}

        # Walk through nums array, keeping track of both index and value
        for i, v in enumerate(nums):

            # Find the complement of the current value
            complement = target - v

            # If we've seen the complement (by key), then return the value at that key, and the current index
            if complement in seen:
                return [seen[complement], i]
            
            # If we haven't seen the complement yet, then add a key:val pair to the dictionary
            else:
                seen[v] = i
