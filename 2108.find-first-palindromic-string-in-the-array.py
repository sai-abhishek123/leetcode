#
# @lc app=leetcode id=2108 lang=python
#
# [2108] Find First Palindromic String in the Array
#
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/
#
# algorithms
# Easy (79.18%)
# Likes:    991
# Dislikes: 32
# Total Accepted:    114.8K
# Total Submissions: 145K
# Testcase Example:  '["abc","car","ada","racecar","cool"]'
#
# Given an array of strings words, return the first palindromic string in the
# array. If there is no such string, return an empty string "".
#
# A string is palindromic if it reads the same forward and backward.
#
#
# Example 1:
#
#
# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.
#
#
# Example 2:
#
#
# Input: words = ["notapalindrome","racecar"]
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".
#
#
# Example 3:
#
#
# Input: words = ["def","ghi"]
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is
# returned.
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists only of lowercase English letters.
#
#
#

# @lc code=start
class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        stre = ""
        for i in range(len(words)):
            stre = words[i][::-1]
            if (stre == words[i]):
                return stre
        return ""
# @lc code=end
