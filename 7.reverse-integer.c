/*
 * @lc app=leetcode id=7 lang=c
 *
 * [7] Reverse Integer
 *
 * https://leetcode.com/problems/reverse-integer/description/
 *
 * algorithms
 * Medium (28.29%)
 * Likes:    12480
 * Dislikes: 13330
 * Total Accepted:    3M
 * Total Submissions: 10.7M
 * Testcase Example:  '123'
 *
 * Given a signed 32-bit integer x, return x with its digits reversed. If
 * reversing x causes the value to go outside the signed 32-bit integer range
 * [-2^31, 2^31 - 1], then return 0.
 *
 * Assume the environment does not allow you to store 64-bit integers (signed
 * or unsigned).
 *
 *
 * Example 1:
 *
 *
 * Input: x = 123
 * Output: 321
 *
 *
 * Example 2:
 *
 *
 * Input: x = -123
 * Output: -321
 *
 *
 * Example 3:
 *
 *
 * Input: x = 120
 * Output: 21
 *
 *
 *
 * Constraints:
 *
 *
 * -2^31 <= x <= 2^31 - 1
 *
 *
 */

// @lc code=start
int reverse(int x)
{
    int temp;
    long int sum = 0;
    temp = x;
    while (temp)
    {
        int rem = temp % 10;
        sum = sum * 10 + rem;
        temp /= 10;
    }
    if (sum > pow(2, 31) || sum < -(pow(2, 31)))
        return 0;
    else
        return sum;
}
// @lc code=end
