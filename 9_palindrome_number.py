class Solution:
    def isPalindrome(self, x):
        # Case for 0
        if x == 0:
            return True
        # Case for the negative, the numbers that can be devided by 10
        if (x<0) or (x%10) == 0:
            return False
        # Calculate the reverse number
        original_number, new_number = x , 0
        while x>=10 :
            new_number, x = new_number * 10 + x % 10 , x // 10
        if new_number == original_number//10:
            return True
        return False

sol = Solution()
print(sol.isPalindrome())
