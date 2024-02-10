#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (63.95%)
# Likes:    18066
# Dislikes: 565
# Total Accepted:    2.4M
# Total Submissions: 3.8M
# Testcase Example:  '[3,2,3]'
#
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You
# may assume that the majority element always exists in the array.
#
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?
#

# @lc code=start
from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1 = Counter(nums)
        nums2 = dict(nums1)
        maxi = max(nums2.values())
        for key, value in nums2.items():
            if value == maxi:
                return key

# @lc code=end
