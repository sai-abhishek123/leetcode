#
# @lc app=leetcode id=1768 lang=python
#
# [1768] Merge Strings Alternately
#
# https://leetcode.com/problems/merge-strings-alternately/description/
#
# algorithms
# Easy (79.35%)
# Likes:    3508
# Dislikes: 73
# Total Accepted:    635K
# Total Submissions: 799.8K
# Testcase Example:  '"abc"\n"pqr"'
#
# You are given two strings word1 and word2. Merge the strings by adding
# letters in alternating order, starting with word1. If a string is longer than
# the other, append the additional letters onto the end of the merged string.
#
# Return the merged string.
#
#
# Example 1:
#
#
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
#
#
# Example 2:
#
#
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s
#
#
# Example 3:
#
#
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q
# merged: a p b q c   d
#
#
#
# Constraints:
#
#
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.
#
#

# @lc code=start
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        final_size = len(word1) + len(word2)
        final_list = [''] * final_size
        final_string = ""
        e = 0
        o = 0
        for i in range(len(final_list)):
            if i % 2 == 0:
                final_list[i] = word1[e]
                e += 1
                if e == len(word1) and len(word1) < len(word2):
                    print(word2[e:])
                    e -= 1
                    final_list.append(word2[e:])
                    break
            elif i % 2 != 0:
                final_list[i] = word2[o]
                o += 1
                if o == len(word2) and len(word2) < len(word1):
                    final_list.append(word1[o:])
                    break
        final_string = ''.join(str(i) for i in final_list)
        return final_string


# @lc code=end
