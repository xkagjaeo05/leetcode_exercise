class Solution:
    def maxSubArray(self, nums) :
        if not nums:
            return 0
        cumSum = maxSum = nums[0]
        for num in nums:
            cumSum = max(cumSum+num, num)
            maxSum = max(maxSum, cumSum)
        return maxSum

sol = Solution()
print(sol.maxSubArray( [-2,1,-3,4,-1,2,1,-5,4] ) )
