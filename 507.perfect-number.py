#
# @lc app=leetcode id=507 lang=python
#
# [507] Perfect Number
#
# https://leetcode.com/problems/perfect-number/description/
#
# algorithms
# Easy (39.52%)
# Likes:    1027
# Dislikes: 1203
# Total Accepted:    170.6K
# Total Submissions: 431.6K
# Testcase Example:  '28'
#
# A perfect number is a positive integer that is equal to the sum of its
# positive divisors, excluding the number itself. A divisor of an integer x is
# an integer that can divide x evenly.
#
# Given an integer n, return true if n is a perfect number, otherwise return
# false.
#
#
# Example 1:
#
#
# Input: num = 28
# Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.
#
#
# Example 2:
#
#
# Input: num = 7
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= num <= 10^8
#
#
#

# @lc code=start
import math


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        sum1 = 1
        sqrt_num = int(math.sqrt(num))
        for i in range(2, sqrt_num+1):
            if num % i == 0:
                sum1 += i
                if i != num//i:
                    sum1 += num//i
        return sum1 == num
# @lc code=end
