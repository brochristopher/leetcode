class Solution:
    def romanToInt(self, s: str) -> int:

        total = 0

        while len(s) > 0:
            if "CM" in s:
                total += 900
                s = s.replace("CM", "", 1)  # Remove one occurrence of "CM"
            elif "CD" in s:
                total += 400
                s = s.replace("CD", "", 1)
            elif "XC" in s:
                total += 90
                s = s.replace("XC", "", 1)
            elif "XL" in s:
                total += 40
                s = s.replace("XL", "", 1)
            elif "IX" in s:
                total += 9
                s = s.replace("IX", "", 1)
            elif "IV" in s:
                total += 4
                s = s.replace("IV", "", 1)
            elif "M" in s:
                total += 1000
                s = s.replace("M", "", 1)
            elif "D" in s:
                total += 500
                s = s.replace("D", "", 1)
            elif "C" in s:
                total += 100
                s = s.replace("C", "", 1)
            elif "L" in s:
                total += 50
                s = s.replace("L", "", 1)
            elif "X" in s:
                total += 10
                s = s.replace("X", "", 1)
            elif "V" in s:
                total += 5
                s = s.replace("V", "", 1)
            elif "I" in s:
                total += 1
                s = s.replace("I", "", 1)

        return total
