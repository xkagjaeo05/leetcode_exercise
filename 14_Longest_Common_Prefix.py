class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest_str = min(strs, key =len)
        for ind, char in enumerate(shortest_str):
            for str_ in strs:
                if char != str_[ind]:
                    return shortest_str[:ind]
        return shortest_str


sol = Solution()
print(sol.longestCommonPrefix(['flower','flour','flow']))
