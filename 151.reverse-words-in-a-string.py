#
# @lc app=leetcode id=151 lang=python
#
# [151] Reverse Words in a String
#
# https://leetcode.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (40.06%)
# Likes:    7933
# Dislikes: 5034
# Total Accepted:    1.3M
# Total Submissions: 3.3M
# Testcase Example:  '"the sky is blue"'
#
# Given an input string s, reverse the order of the words.
#
# A word is defined as a sequence of non-space characters. The words in s will
# be separated by at least one space.
#
# Return a string of the words in reverse order concatenated by a single
# space.
#
# Note that s may contain leading or trailing spaces or multiple spaces between
# two words. The returned string should only have a single space separating the
# words. Do not include any extra spaces.
#
#
# Example 1:
#
#
# Input: s = "the sky is blue"
# Output: "blue is sky the"
#
#
# Example 2:
#
#
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing
# spaces.
#
#
# Example 3:
#
#
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single
# space in the reversed string.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s contains English letters (upper-case and lower-case), digits, and spaces '
# '.
# There is at least one word in s.
#
#
#
# Follow-up: If the string data type is mutable in your language, can you solve
# it in-place with O(1) extra space?
#
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        b = []
        a = []
        m = ""
        a = s.split(" ")
        for i in range(len(a)):
            if (a[i] != ""):
                b.append(a[i])
        b.reverse()
        for i in range(len(b)):
            m = m+" "+b[i]
        final_string = m.strip()
        return final_string
# @lc code=end
