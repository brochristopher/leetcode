class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = ""
        carry_over = "0"

        while len(a) > len(b):
            b = "0" + b
        while len(b) > len(a):
            a = "0" + a
            
        a = "0" + a 
        b = "0" + b

        for (i,j) in zip(a[::-1], b[::-1]):
            if int(i) + int(j) + int(carry_over) == 0:
                c = "0" + c
                carry_over = False
            elif int(i) + int(j) + int(carry_over) == 1:
                c = "1" + c
                carry_over = False
            elif int(i) + int(j) + int(carry_over) == 2:
                c = "0" + c
                carry_over = True
            elif int(i) + int(j) + int(carry_over) == 3:
                c = "1" + c
                carry_over = True
            
        if c[0] == "0":
            c = c.replace("0", "", 1)

        return(c)
