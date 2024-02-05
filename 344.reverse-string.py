#
# @lc app=leetcode id=344 lang=python
#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (77.54%)
# Likes:    8181
# Dislikes: 1145
# Total Accepted:    2.4M
# Total Submissions: 3.1M
# Testcase Example:  '["h","e","l","l","o"]'
#
# Write a function that reverses a string. The input string is given as an
# array of characters s.
#
# You must do this by modifying the input array in-place with O(1) extra
# memory.
#
#
# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s[i] is a printable ascii character.
#
#
#

# @lc code=start
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        sum1 = ""
        for i in range(len(s)):
            sum1 = sum1+s[i]
        sum2 = sum1[::-1]
        a = [""]*len(sum2)
        for i in range(len(sum2)):
            s[i] = sum2[i]
        return s
# @lc code=end
