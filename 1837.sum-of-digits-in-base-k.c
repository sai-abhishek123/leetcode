/*
 * @lc app=leetcode id=1837 lang=c
 *
 * [1837] Sum of Digits in Base K
 *
 * https://leetcode.com/problems/sum-of-digits-in-base-k/description/
 *
 * algorithms
 * Easy (77.14%)
 * Likes:    493
 * Dislikes: 44
 * Total Accepted:    49.8K
 * Total Submissions: 64.6K
 * Testcase Example:  '34\n6'
 *
 * Given an integer n (in base 10) and a base k, return the sum of the digits
 * of n after converting n from base 10 to base k.
 *
 * After converting, each digit should be interpreted as a base 10 number, and
 * the sum should be returned in base 10.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 34, k = 6
 * Output: 9
 * Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.
 *
 *
 * Example 2:
 *
 *
 * Input: n = 10, k = 10
 * Output: 1
 * Explanation: n is already in base 10. 1 + 0 = 1.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 100
 * 2 <= k <= 10
 *
 *
 */

// @lc code=start
int reverse(int n)
{
    int sum = 0, rem, temp = n, sum1 = 0;
    while (n)
    {
        rem = n % 10;
        sum = sum * 10 + rem;
        n /= 10;
    }
    while (sum)
    {
        rem = sum % 10;
        sum1 += rem;
        sum /= 10;
    }
    return sum1;
}
int sumBase(int n, int k)
{
    int rem, sum = 0;
    while (n)
    {
        rem = n % k;
        sum = sum * 10 + rem;
        n /= k;
    }
    return (reverse(sum));
}
// @lc code=end
