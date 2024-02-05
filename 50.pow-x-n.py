#
# @lc app=leetcode id=50 lang=python
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (34.35%)
# Likes:    9260
# Dislikes: 9166
# Total Accepted:    1.5M
# Total Submissions: 4.4M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
#
#
# Example 1:
#
#
# Input: x = 2.00000, n = 10
# Output: 1024.00000
#
#
# Example 2:
#
#
# Input: x = 2.10000, n = 3
# Output: 9.26100
#
#
# Example 3:
#
#
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
#
#
#
# Constraints:
#
#
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# n is an integer.
# Either x is not zero or n > 0.
# -10^4 <= x^n <= 10^4
#
#
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return (pow(x, n))


# @lc code=end
