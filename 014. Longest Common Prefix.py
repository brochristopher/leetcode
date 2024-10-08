class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        largestPrefix = ""
        
        # If the list is empty, return an empty string
        if len(strs) == 0:
            return ""
        
        # If the list has only one string, return that string
        if len(strs) == 1:
            return strs[0]
        
        # Iterate over the characters by index
        for currentLetterIndex in range(len(strs[0])):
            currentPrefix = strs[0][currentLetterIndex]
            
            # Check each string in the list
            for string in strs:
                # Guard condition to avoid index out of range
                if currentLetterIndex >= len(string) or string[currentLetterIndex] != currentPrefix:
                    return largestPrefix  # Return the prefix found so far
            
            # If all strings have the same character at the current index, add it to the prefix
            largestPrefix += currentPrefix
        
        return largestPrefix
