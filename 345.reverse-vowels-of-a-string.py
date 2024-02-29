#
# @lc app=leetcode id=345 lang=python
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (52.38%)
# Likes:    4352
# Dislikes: 2757
# Total Accepted:    768.9K
# Total Submissions: 1.5M
# Testcase Example:  '"hello"'
#
# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
# and upper cases, more than once.
#
#
# Example 1:
# Input: s = "hello"
# Output: "holle"
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"
#
#
# Constraints:
#
#
# 1 <= s.length <= 3 * 10^5
# s consist of printable ASCII characters.
#
#
#

# @lc code=start
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        final_string = ""
        list_s = list(s)
        vowels = []
        check_string = 'AEIOUaeiou'
        for i in range(len(list_s)):
            if list_s[i] in check_string:
                vowels.append(list_s[i])
                list_s[i] = 0
        vowels_reverse = vowels[::-1]
        j = 0
        for i in range(len(list_s)):
            if list_s[i] == 0:
                list_s[i] = vowels_reverse[j]
                j += 1
        for i in range(len(list_s)):
            final_string += list_s[i]
        return final_string

# @lc code=end
