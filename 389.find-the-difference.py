#
# @lc app=leetcode id=389 lang=python
#
# [389] Find the Difference
#
# https://leetcode.com/problems/find-the-difference/description/
#
# algorithms
# Easy (59.98%)
# Likes:    4864
# Dislikes: 469
# Total Accepted:    688.5K
# Total Submissions: 1.1M
# Testcase Example:  '"abcd"\n"abcde"'
#
# You are given two strings s and t.
#
# String t is generated by random shuffling string s and then add one more
# letter at a random position.
#
# Return the letter that was added to t.
#
#
# Example 1:
#
#
# Input: s = "abcd", t = "abcde"
# Output: "e"
# Explanation: 'e' is the letter that was added.
#
#
# Example 2:
#
#
# Input: s = "", t = "y"
# Output: "y"
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 1000
# t.length == s.length + 1
# s and t consist of lowercase English letters.
#
#
#

# @lc code=start
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        new_s = list(s)
        new_t = list(t)
        new_s.sort()
        new_t.sort()
        if len(new_s) > len(new_t):
            new_t.extend([0]*(len(new_s)-len(new_t)))
        elif len(new_t) > len(new_s):
            new_s.extend([0]*(len(new_t)-len(new_s)))
        size = max(len(new_s), len(new_t))
        for i in range(size):
            if str(new_s[i]) != str(new_t[i]):
                if (type(new_s[i])) == 'int':
                    return new_s[i]
                else:
                    return new_t[i]

# @lc code=end