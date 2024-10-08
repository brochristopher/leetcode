class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sorted_s = [*s]
        sorted_s.sort()

        sorted_t = [*t]
        sorted_t.sort()

        if sorted_s == sorted_t:
            return True
