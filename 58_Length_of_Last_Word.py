class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        for char in reversed(s):
            if char.isspace():
                if cnt:
                    break
            else:
                cnt += 1
        return cnt

sol = Solution()
print(sol.lengthOfLastWord('a '))

