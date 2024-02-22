#
# @lc app=leetcode id=263 lang=python
#
# [263] Ugly Number
#
# https://leetcode.com/problems/ugly-number/description/
#
# algorithms
# Easy (41.96%)
# Likes:    3225
# Dislikes: 1669
# Total Accepted:    486.4K
# Total Submissions: 1.2M
# Testcase Example:  '6'
#
# An ugly number is a positive integer whose prime factors are limited to 2, 3,
# and 5.
#
# Given an integer n, return true if n is an ugly number.
#
#
# Example 1:
#
#
# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
#
#
# Example 2:
#
#
# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors, therefore all of its prime factors are
# limited to 2, 3, and 5.
#
#
# Example 3:
#
#
# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.
#
#
#
# Constraints:
#
#
# -2^31 <= n <= 2^31 - 1
#
#
#

# @lc code=start
class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 or n == 2 or n == 3 or n == 5:
            return True
        else:
            while n > 0:
                if n % 2 == 0:
                    n /= 2
                elif n % 3 == 0:
                    n /= 3
                elif n % 5 == 0:
                    n /= 5
                else:
                    if n == 1:
                        return True
                    return False

# @lc code=end
