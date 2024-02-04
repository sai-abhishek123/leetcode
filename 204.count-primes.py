#
# @lc app=leetcode id=204 lang=python
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Medium (33.45%)
# Likes:    7684
# Dislikes: 1403
# Total Accepted:    823.2K
# Total Submissions: 2.5M
# Testcase Example:  '10'
#
# Given an integer n, return the number of prime numbers that are strictly less
# than n.
#
#
# Example 1:
#
#
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
#
# Example 2:
#
#
# Input: n = 0
# Output: 0
#
#
# Example 3:
#
#
# Input: n = 1
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= n <= 5 * 10^6
#
#
#

# @lc code=start
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False

        return sum(is_prime)

# @lc code=end
