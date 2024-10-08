class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        listified_s = []
        listified_t = []

        for i in s:
            listified_s.append(i)

        for i in t:
            listified_t.append(i)

        listified_s.sort()
        listified_t.sort()

        s = ""
        t = ""

        for i in listified_s:
            s += i

        for i in listified_t:
            t += i

        if s == t:
            return True
