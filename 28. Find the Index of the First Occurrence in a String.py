class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleLength = len(needle)
        haystackLength = len(haystack)

        if needle in haystack:
            for i in range(haystackLength):
                if haystack[i:i+needleLength] == needle:
                    return(i)
        else:
            return -1
