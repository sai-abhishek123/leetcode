#
# @lc app=leetcode id=1822 lang=python
#
# [1822] Sign of the Product of an Array
#
# https://leetcode.com/problems/sign-of-the-product-of-an-array/description/
#
# algorithms
# Easy (65.28%)
# Likes:    2114
# Dislikes: 212
# Total Accepted:    319.9K
# Total Submissions: 490K
# Testcase Example:  '[-1,-2,-3,-4,3,2,1]'
#
# There is a function signFunc(x) that returns:
#
#
# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
#
#
# You are given an integer array nums. Let product be the product of all values
# in the array nums.
#
# Return signFunc(product).
#
#
# Example 1:
#
#
# Input: nums = [-1,-2,-3,-4,3,2,1]
# Output: 1
# Explanation: The product of all values in the array is 144, and signFunc(144)
# = 1
#
#
# Example 2:
#
#
# Input: nums = [1,5,0,2,-3]
# Output: 0
# Explanation: The product of all values in the array is 0, and signFunc(0) =
# 0
#
#
# Example 3:
#
#
# Input: nums = [-1,1,-1,1,-1]
# Output: -1
# Explanation: The product of all values in the array is -1, and signFunc(-1) =
# -1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# -100 <= nums[i] <= 100
#
#
#

# @lc code=start
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negative_count = 0
        positive_count = 0
        if 0 in nums:
            return 0
        else:
            nums.sort()
            for i in range(len(nums)):
                if nums[i] < 0:
                    negative_count += 1
                elif nums[i] > 0:
                    positive_count += 1
            if negative_count % 2 == 0:
                return 1
            else:
                return -1

# @lc code=end
