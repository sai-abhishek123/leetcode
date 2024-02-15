#
# @lc app=leetcode id=645 lang=python
#
# [645] Set Mismatch
#
# https://leetcode.com/problems/set-mismatch/description/
#
# algorithms
# Easy (44.61%)
# Likes:    4590
# Dislikes: 1130
# Total Accepted:    428.9K
# Total Submissions: 962.3K
# Testcase Example:  '[1,2,2,4]'
#
# You have a set of integers s, which originally contains all the numbers from
# 1 to n. Unfortunately, due to some error, one of the numbers in s got
# duplicated to another number in the set, which results in repetition of one
# number and loss of another number.
#
# You are given an integer array nums representing the data status of this set
# after the error.
#
# Find the number that occurs twice and the number that is missing and return
# them in the form of an array.
#
#
# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:
# Input: nums = [1,1]
# Output: [1,2]
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^4
#
#
#

# @lc code=start
from collections import Counter


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list_of_items = Counter(nums)
        list_of_items = dict(list_of_items)
        value_set = []
        final_answer = []
        x = 0
        for key, value in list_of_items.items():
            value_set.append(key)
            if value == 2:
                x = key
        final_answer.append(x)
        r = 0
        length = len(value_set)+1
        sume = length*(length+1)//2
        asum = sum(value_set)
        r = sume-asum
        final_answer.append(r)
        return final_answer

# @lc code=end
