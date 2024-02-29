#
# @lc app=leetcode id=387 lang=python
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (60.56%)
# Likes:    8841
# Dislikes: 289
# Total Accepted:    1.7M
# Total Submissions: 2.7M
# Testcase Example:  '"leetcode"'
#
# Given a string s, find the first non-repeating character in it and return its
# index. If it does not exist, return -1.
#
#
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# Input: s = "aabb"
# Output: -1
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of only lowercase English letters.
#
#
#

# @lc code=start
from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        final_dict = dict(Counter(s))
        final_ls = list(s)
        for i in range(len(final_ls)):
            if final_dict.get(final_ls[i], 0) == 1:
                return i
        return -1

# @lc code=end
