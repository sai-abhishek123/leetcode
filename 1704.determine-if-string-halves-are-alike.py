#
# @lc app=leetcode id=1704 lang=python
#
# [1704] Determine if String Halves Are Alike
#
# https://leetcode.com/problems/determine-if-string-halves-are-alike/description/
#
# algorithms
# Easy (78.75%)
# Likes:    2203
# Dislikes: 124
# Total Accepted:    338.4K
# Total Submissions: 429.7K
# Testcase Example:  '"book"'
#
# You are given a string s of even length. Split this string into two halves of
# equal lengths, and let a be the first half and b be the second half.
#
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i',
# 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and
# lowercase letters.
#
# Return true if a and b are alike. Otherwise, return false.
#
#
# Example 1:
#
#
# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel.
# Therefore, they are alike.
#
#
# Example 2:
#
#
# Input: s = "textbook"
# Output: false
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2.
# Therefore, they are not alike.
# Notice that the vowel o is counted twice.
#
#
#
# Constraints:
#
#
# 2 <= s.length <= 1000
# s.length is even.
# s consists of uppercase and lowercase letters.
#
#
#

# @lc code=start
class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        length_2 = len(s)/2
        a = [""]*length_2
        b = [""]*length_2
        for i in range(0, length/2, 1):
            a[i] = s[i].lower()
        for i in range(length/2, length, 1):
            b[length/2-i] = s[i].lower()
        c1 = 0
        c2 = 0
        for i in range(len(a)):
            if (a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u'):
                c1 += 1
        for i in range(len(b)):
            if (b[i] == 'a' or b[i] == 'e' or b[i] == 'i' or b[i] == 'o' or b[i] == 'u'):
                c2 += 1
        if (c1 == c2):
            return True
        else:
            return False

# @lc code=end
