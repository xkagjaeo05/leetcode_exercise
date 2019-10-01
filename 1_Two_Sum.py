
class Solution:
    def twoSum(self, nums, target : int):
        h = {}
        for ind, num in enumerate(nums):
            diff = target - num
            if num in h :
                return [ h[num], ind ]
            else:
                h[diff] = ind
        return []

sol = Solution()
print( sol.twoSum([2, 7, 11, 15],9) )
