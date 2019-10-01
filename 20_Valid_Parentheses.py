class Solution:
    def isValid(self, s) :
        pair_dict = {')':'(',
                     '}':'{',
                     ']':'['}
        # Case for empty string
        if len(s) == 0:
            return True
        # The other cases
        stack = []
        for char in s:
            if char not in pair_dict:
                stack.append(char)
            else:
                if len(stack)>0 and pair_dict[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack

sol = Solution()
print(sol.isValid('{}[]()'))
