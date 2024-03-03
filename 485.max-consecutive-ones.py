#
# @lc app=leetcode id=485 lang=python
#
# [485] Max Consecutive Ones
#
# https://leetcode.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (58.40%)
# Likes:    5529
# Dislikes: 452
# Total Accepted:    1.1M
# Total Submissions: 1.9M
# Testcase Example:  '[1,1,0,1,1,1]'
#
# Given a binary array nums, return the maximum number of consecutive 1's in
# the array.
#
#
# Example 1:
#
#
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive
# 1s. The maximum number of consecutive 1s is 3.
#
#
# Example 2:
#
#
# Input: nums = [1,0,1,1,0,1]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
#
#
#

# @lc code=start
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == 1:
                return 1
            return 0
        count = 0
        ca = []
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            elif nums[i] == 0:
                ca.append(count)
                count = 0~
        if len(ca) == 0:
            return count
        return (max(count, max(ca)))
# @lc code=end
