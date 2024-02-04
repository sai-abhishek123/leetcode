#
# @lc app=leetcode id=442 lang=python
#
# [442] Find All Duplicates in an Array
#
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
#
# algorithms
# Medium (73.60%)
# Likes:    9502
# Dislikes: 338
# Total Accepted:    595.6K
# Total Submissions: 809.2K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an integer array nums of length n where all the integers of nums are in
# the range [1, n] and each integer appears once or twice, return an array of
# all the integers that appears twice.
#
# You must write an algorithm that runs in O(n) time and uses only constant
# extra space.
#
#
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:
# Input: nums = [1,1,2]
# Output: [1]
# Example 3:
# Input: nums = [1]
# Output: []
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 10^5
# 1 <= nums[i] <= n
# Each element in nums appears once or twice.
#
#
#

# @lc code=start
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        nums.sort()
        for i in range(1, len(nums)):
            if (nums[i-1] == nums[i] and nums[i] not in answer):
                answer.append(nums[i])
        return answer
# @lc code=end
