#
# @lc app=leetcode id=747 lang=python
#
# [747] Largest Number At Least Twice of Others
#
# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
#
# algorithms
# Easy (48.40%)
# Likes:    1162
# Dislikes: 884
# Total Accepted:    232.8K
# Total Submissions: 481K
# Testcase Example:  '[3,6,1,0]'
#
# You are given an integer array nums where the largest integer is unique.
#
# Determine whether the largest element in the array is at least twice as much
# as every other number in the array. If it is, return the index of the largest
# element, or return -1 otherwise.
#
#
# Example 1:
#
#
# Input: nums = [3,6,1,0]
# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4]
# Output: -1
# Explanation: 4 is less than twice the value of 3, so we return -1.
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 50
# 0 <= nums[i] <= 100
# The largest element in nums is unique.
#
#
#

# @lc code=start
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = max(nums)
        c = 0
        a = []
        for i in range(len(nums)):
            if (nums[i] != maxi):
                a.append(nums[i])
        for i in range(len(a)):
            if (maxi >= (2*a[i])):
                c += 1
            else:
                return -1
        return nums.index(maxi)

# @lc code=end
