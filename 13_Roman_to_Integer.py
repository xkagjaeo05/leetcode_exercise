class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_dict = {'I':1,
                       'V':5,
                       'X':10,
                       'L':50,
                       'C':100,
                       'D':500,
                       'M':1000}
        sum_, last_string = 0 , 'I'
        for string_ in s[::-1]:
            if symbol_dict[string_] < symbol_dict[last_string]:
                sum_ , last_string = sum_ - symbol_dict[string_], string_
            else:
                sum_ , last_string = sum_ + symbol_dict[string_], string_
        return sum_

sol = Solution()
print( sol.romanToInt('III') )
