class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = ""

        for i in digits:
            str_digits += str(i)
            
        new_digit = int(str_digits)

        new_digit += 1

        str_digits = str(new_digit)

        new_array = []

        for i in str_digits:
            new_array.append(int(i))
            
        return(new_array)
