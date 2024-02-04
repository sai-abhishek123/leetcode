/*
 * @lc app=leetcode id=2413 lang=c
 *
 * [2413] Smallest Even Multiple
 *
 * https://leetcode.com/problems/smallest-even-multiple/description/
 *
 * algorithms
 * Easy (87.59%)
 * Likes:    840
 * Dislikes: 96
 * Total Accepted:    142K
 * Total Submissions: 162.2K
 * Testcase Example:  '5'
 *
 * Given a positive integer n, return the smallest positive integer that is a
 * multiple of both 2 and n.
 *
 * Example 1:
 *
 *
 * Input: n = 5
 * Output: 10
 * Explanation: The smallest multiple of both 5 and 2 is 10.
 *
 *
 * Example 2:
 *
 *
 * Input: n = 6
 * Output: 6
 * Explanation: The smallest multiple of both 6 and 2 is 6. Note that a number
 * is a multiple of itself.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 150
 *
 *
 */

// @lc code=start
int smallestEvenMultiple(int n)
{
    int b = n % 2;
    if (b == 1)
        return n * 2;
    else
        return n;
}
// @lc code=end
