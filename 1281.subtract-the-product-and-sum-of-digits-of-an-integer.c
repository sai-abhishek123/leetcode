/*
 * @lc app=leetcode id=1281 lang=c
 *
 * [1281] Subtract the Product and Sum of Digits of an Integer
 *
 * https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/
 *
 * algorithms
 * Easy (86.38%)
 * Likes:    2485
 * Dislikes: 226
 * Total Accepted:    460.4K
 * Total Submissions: 533K
 * Testcase Example:  '234'
 *
 * Given an integer number n, return the difference between the product of its
 * digits and the sum of its digits.
 *
 * Example 1:
 *
 *
 * Input: n = 234
 * Output: 15
 * Explanation:
 * Product of digits = 2 * 3 * 4 = 24
 * Sum of digits = 2 + 3 + 4 = 9
 * Result = 24 - 9 = 15
 *
 *
 * Example 2:
 *
 *
 * Input: n = 4421
 * Output: 21
 * Explanation:
 * Product of digits = 4 * 4 * 2 * 1 = 32
 * Sum of digits = 4 + 4 + 2 + 1 = 11
 * Result = 32 - 11 = 21
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 10^5
 *
 *
 */

// @lc code=start
int subtractProductAndSum(int n)
{
    int count = 0, i, j, k, prod = 1, sum = 0, diff;
    int temp = n;
    while (temp)
    {
        int rem = temp % 10;
        count++;
        temp /= 10;
    }
    int a[count];
    for (i = 0; i < count; i++)
    {
        int rem = n % 10;
        a[i] = rem;
        n /= 10;
    }
    for (i = 0; i < count; i++)
    {
        prod *= a[i];
        sum += a[i];
    }
    diff = prod - sum;
    return diff;
}
// @lc code=end
