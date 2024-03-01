#
# @lc app=leetcode id=434 lang=python
#
# [434] Number of Segments in a String
#
# https://leetcode.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (36.46%)
# Likes:    767
# Dislikes: 1251
# Total Accepted:    173.1K
# Total Submissions: 475.2K
# Testcase Example:  '"Hello, my name is John"'
#
# Given a string s, return the number of segments in the string.
#
# A segment is defined to be a contiguous sequence of non-space characters.
#
#
# Example 1:
#
#
# Input: s = "Hello, my name is John"
# Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
#
#
# Example 2:
#
#
# Input: s = "Hello"
# Output: 1
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 300
# s consists of lowercase and uppercase English letters, digits, or one of the
# following characters "!@#$%^&*()_+-=',.:".
# The only space character in s is ' '.
#
#
#

# @lc code=start
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        if len(s) == 0:
            return 0
        a = s.split(" ")
        for i in range(len(a)):
            if a[i] != "":
                count += 1
        return count
        return len(s.split())
# @lc code=end
