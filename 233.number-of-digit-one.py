#
# @lc app=leetcode id=233 lang=python
#
# [233] Number of Digit One
#
# https://leetcode.com/problems/number-of-digit-one/description/
#
# algorithms
# Hard (34.37%)
# Likes:    1477
# Dislikes: 1439
# Total Accepted:    88.2K
# Total Submissions: 256.5K
# Testcase Example:  '13'
#
# Given an integer n, count the total number of digit 1 appearing in all
# non-negative integers less than or equal to n.
#
#
# Example 1:
#
#
# Input: n = 13
# Output: 6
#
#
# Example 2:
#
#
# Input: n = 0
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= n <= 10^9
#
#
#

# @lc code=start
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        factor = 1
        while factor <= n:
            higher = n // (factor * 10)
            current = (n // factor) % 10
            lower = n % factor
            if current == 0:
                count += higher * factor
            elif current == 1:
                count += higher * factor + lower + 1
            else:
                count += (higher + 1) * factor
            factor *= 10
        return count

# @lc code=end
