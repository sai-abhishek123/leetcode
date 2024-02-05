#
# @lc app=leetcode id=2278 lang=python
#
# [2278] Percentage of Letter in String
#
# https://leetcode.com/problems/percentage-of-letter-in-string/description/
#
# algorithms
# Easy (73.77%)
# Likes:    485
# Dislikes: 54
# Total Accepted:    64.8K
# Total Submissions: 87.9K
# Testcase Example:  '"foobar"\n"o"'
#
# Given a string s and a character letter, return the percentage of characters
# in s that equal letter rounded down to the nearest whole percent.
#
#
# Example 1:
#
#
# Input: s = "foobar", letter = "o"
# Output: 33
# Explanation:
# The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% =
# 33% when rounded down, so we return 33.
#
#
# Example 2:
#
#
# Input: s = "jjjj", letter = "k"
# Output: 0
# Explanation:
# The percentage of characters in s that equal the letter 'k' is 0%, so we
# return 0.
#
#
# Constraints:
#
#
# 1 <= s.length <= 100
# s consists of lowercase English letters.
# letter is a lowercase English letter.
#
#
#

# @lc code=start
class Solution(object):
    def percentageLetter(self, s, letter):
        count = 0
        for i in range(len(s)):
            if letter == s[i]:
                count += 1
        percent = float(count) / len(s) * 100
        return int(percent)

# @lc code=end
