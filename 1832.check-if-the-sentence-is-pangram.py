#
# @lc app=leetcode id=1832 lang=python
#
# [1832] Check if the Sentence Is Pangram
#
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/
#
# algorithms
# Easy (83.06%)
# Likes:    2669
# Dislikes: 52
# Total Accepted:    307.6K
# Total Submissions: 370.1K
# Testcase Example:  '"thequickbrownfoxjumpsoverthelazydog"'
#
# A pangram is a sentence where every letter of the English alphabet appears at
# least once.
#
# Given a string sentence containing only lowercase English letters, return
# true if sentence is a pangram, or false otherwise.
#
#
# Example 1:
#
#
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English
# alphabet.
#
#
# Example 2:
#
#
# Input: sentence = "leetcode"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.
#
#
#

# @lc code=start
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        return len(set(sentence)) == 26
# @lc code=end
