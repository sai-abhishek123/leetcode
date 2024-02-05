/*
 * @lc app=leetcode id=2520 lang=c
 *
 * [2520] Count the Digits That Divide a Number
 *
 * https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/
 *
 * algorithms
 * Easy (83.92%)
 * Likes:    462
 * Dislikes: 30
 * Total Accepted:    69.2K
 * Total Submissions: 82.5K
 * Testcase Example:  '7'
 *
 * Given an integer num, return the number of digits in num that divide num.
 *
 * An integer val divides nums if nums % val == 0.
 *
 *
 * Example 1:
 *
 *
 * Input: num = 7
 * Output: 1
 * Explanation: 7 divides itself, hence the answer is 1.
 *
 *
 * Example 2:
 *
 *
 * Input: num = 121
 * Output: 2
 * Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a
 * digit, we return 2.
 *
 *
 * Example 3:
 *
 *
 * Input: num = 1248
 * Output: 4
 * Explanation: 1248 is divisible by all of its digits, hence the answer is
 * 4.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= num <= 10^9
 * num does not contain 0 as one of its digits.
 *
 *
 */

// @lc code=start
int countDigits(int num)
{
    int count = 0;
    int temp = num;
    while (temp)
    {
        int rem = temp % 10;
        if (num % rem == 0)
        {
            count++;
        }
        temp /= 10;
    }
    return count;
}
// @lc code=end
