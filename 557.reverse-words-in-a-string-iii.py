#
# @lc app=leetcode id=557 lang=python
#
# [557] Reverse Words in a String III
#
# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (82.95%)
# Likes:    5803
# Dislikes: 244
# Total Accepted:    870K
# Total Submissions: 1M
# Testcase Example:  `"Let's take LeetCode contest"`
#
# Given a string s, reverse the order of characters in each word within a
# sentence while still preserving whitespace and initial word order.
#
#
# Example 1:
#
#
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#
#
# Example 2:
#
#
# Input: s = "Mr Ding"
# Output: "rM gniD"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 5 * 10^4
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.
#
#
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s.split(" ")
        sum1 = ""
        for i in range(len(a)):
            a[i] = a[i][::-1]
        for i in range(len(a)):
            if (i == 0):
                sum1 = sum1+a[i]
            else:
                sum1 = sum1+" "+a[i]
        return sum1
# @lc code=end
