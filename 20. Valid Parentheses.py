class Solution:
    def isValid(self, s: str) -> bool:
        valid_parens = ["()","[]","{}"]

        for i in s: 
            for j in valid_parens:
                s = s.replace(j, "")

                if len(s) == 0:
                    return(True)
                
                if len(s) % 2 != 0:
                    return (False)
