class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringified_num = str(x)
        listified_num = []

        if stringified_num[0] == "-":
            return(False)
        else:
            for i in stringified_num:
                listified_num.append(i)
        
        reversed_listified_num = listified_num[::-1]

        if listified_num == reversed_listified_num:
            return(True)
        else:
            return(False)
