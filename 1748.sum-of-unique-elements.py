#
# @lc app=leetcode id=1748 lang=python
#
# [1748] Sum of Unique Elements
#
# https://leetcode.com/problems/sum-of-unique-elements/description/
#
# algorithms
# Easy (77.17%)
# Likes:    1487
# Dislikes: 33
# Total Accepted:    153.2K
# Total Submissions: 198.4K
# Testcase Example:  '[1,2,3,2]'
#
# You are given an integer array nums. The unique elements of an array are the
# elements that appear exactly once in the array.
#
# Return the sum of all the unique elements of nums.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.
#
#
# Example 2:
#
#
# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.
#
#
# Example 3:
#
#
# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
#
#
#

# @lc code=start
from collections import Counter


class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        listing = Counter(nums)
        dictionary = dict(listing)
        sum1 = 0
        for key, value in dictionary.items():
            if value == 1:
                sum1 += key
        return sum1
# @lc code=end
