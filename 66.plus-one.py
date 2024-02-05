#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (44.79%)
# Likes:    8884
# Dislikes: 5321
# Total Accepted:    2.1M
# Total Submissions: 4.6M
# Testcase Example:  '[1,2,3]'
#
# You are given a large integer represented as an integer array digits, where
# each digits[i] is the i^th digit of the integer. The digits are ordered from
# most significant to least significant in left-to-right order. The large
# integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of
# digits.
#
#
# Example 1:
#
#
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
#
#
# Example 2:
#
#
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
#
#
# Example 3:
#
#
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
#
#
#
# Constraints:
#
#
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.
#
#
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        count = 0
        sum = 0
        for i in range(len(digits)):
            sum = sum*10+digits[i]
        sum = sum+1
        sum1 = sum
        while (sum1):
            rem = sum1 % 10
            count = count+1
            sum1 = sum1/10
        arr = [0]*count
        # for i in range(arr[count]):
        for i in range(len(arr)):
            rem = sum % 10
            arr[i] = rem
            sum = sum/10
        rev_arr = arr[::-1]
        return rev_arr
# @lc code=end
