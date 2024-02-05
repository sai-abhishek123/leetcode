#
# @lc app=leetcode id=709 lang=python
#
# [709] To Lower Case
#
# https://leetcode.com/problems/to-lower-case/description/
#
# algorithms
# Easy (83.04%)
# Likes:    1780
# Dislikes: 2757
# Total Accepted:    487.4K
# Total Submissions: 586.9K
# Testcase Example:  '"Hello"'
#
# Given a string s, return the string after replacing every uppercase letter
# with the same lowercase letter.
#
#
# Example 1:
#
#
# Input: s = "Hello"
# Output: "hello"
#
#
# Example 2:
#
#
# Input: s = "here"
# Output: "here"
#
#
# Example 3:
#
#
# Input: s = "LOVELY"
# Output: "lovely"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 100
# s consists of printable ASCII characters.
#
#
#

# @lc code=start
class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s.lower()

# @lc code=end
