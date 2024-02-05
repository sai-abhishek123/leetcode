#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (53.13%)
# Likes:    9134
# Dislikes: 931
# Total Accepted:    1.4M
# Total Submissions: 2.6M
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings a and b, return their sum as a binary string.
#
#
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
# Constraints:
#
#
# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
#
#
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum1 = 0
        c = int(a)
        d = int(b)
        for i in range(len(a)):
            rem = c % 10
            sum1 = sum1+pow(2, i)*rem
            c = c/10
        sum2 = 0
        for i in range(len(b)):
            rem = d % 10
            sum2 = sum2+pow(2, i)*rem
            d /= 10
        e = sum1+sum2
        return str(bin(e)[2:])


# @lc code=end
