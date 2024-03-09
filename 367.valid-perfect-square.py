#
# @lc app=leetcode id=367 lang=python
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (43.55%)
# Likes:    4102
# Dislikes: 298
# Total Accepted:    569.2K
# Total Submissions: 1.3M
# Testcase Example:  '16'
#
# Given a positive integer num, return true if num is a perfect square or false
# otherwise.
#
# A perfect square is an integer that is the square of an integer. In other
# words, it is the product of some integer with itself.
#
# You must not use any built-in library function, such as sqrt.
#
#
# Example 1:
#
#
# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
#
#
# Example 2:
#
#
# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an
# integer.
#
#
#
# Constraints:
#
#
# 1 <= num <= 2^31 - 1
#
#
#

# @lc code=start
import math


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = math.sqrt(num)
        y = math.floor(x)
        if (x-y == 0):
            return True
        return False

# @lc code=end
