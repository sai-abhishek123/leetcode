/*
 * @lc app=leetcode id=202 lang=c
 *
 * [202] Happy Number
 *
 * https://leetcode.com/problems/happy-number/description/
 *
 * algorithms
 * Easy (55.78%)
 * Likes:    9950
 * Dislikes: 1367
 * Total Accepted:    1.4M
 * Total Submissions: 2.4M
 * Testcase Example:  '19'
 *
 * Write an algorithm to determine if a number n is happy.
 *
 * A happy number is a number defined by the following process:
 *
 *
 * Starting with any positive integer, replace the number by the sum of the
 * squares of its digits.
 * Repeat the process until the number equals 1 (where it will stay), or it
 * loops endlessly in a cycle which does not include 1.
 * Those numbers for which this process ends in 1 are happy.
 *
 *
 * Return true if n is a happy number, and false if not.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 19
 * Output: true
 * Explanation:
 * 1^2 + 9^2 = 82
 * 8^2 + 2^2 = 68
 * 6^2 + 8^2 = 100
 * 1^2 + 0^2 + 0^2 = 1
 *
 *
 * Example 2:
 *
 *
 * Input: n = 2
 * Output: false
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 2^31 - 1
 *
 *
 */

// @lc code=start
#include <math.h>
int count(int n)
{
    int count = 0;
    while (n)
    {
        int temp = n % 10;
        count++;
        n /= 10;
    }
    return count;
}
int summer(int n)
{
    int sum = 0;
    while (n)
    {
        int temp = n % 10;
        sum += pow(temp, 2);
        n /= 10;
    }
    return sum;
}
bool isHappy(int n)
{
    if (n == 7)
    {
        return true;
    }
    while (count(n) > 1)
    {
        n = summer(n);
        // printf("%d\n",n);
        if (n == 7)
        {
            return true;
        }
    }
    if (n == 1 && count(n) == 1)
    {
        return true;
    }
    return false;
}
// @lc code=end
