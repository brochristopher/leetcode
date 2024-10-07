class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercased = s.lower()
        alphanumeric = ""
        reversed = ""
     
        for i in lowercased:
            if i in "abcdefghijklmnopqrstuvwxyz0123456789":
                alphanumeric += i
        
        for i in alphanumeric[::-1]:
            reversed += i

        if alphanumeric == reversed:
            return True
        else:
            return False
