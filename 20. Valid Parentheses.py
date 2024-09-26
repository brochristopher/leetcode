class Solution:
    def isValid(self, s: str) -> bool:
        valid_parens = ["()","[]","{}"]

        if len(s) % 2 != 0:
                    return (False)

        for i in s: 
            for j in valid_parens:
                s = s.replace(j, "")

                if len(s) == 0:
                    return(True)
