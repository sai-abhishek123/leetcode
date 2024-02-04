/*
 * @lc app=leetcode id=2119 lang=c
 *
 * [2119] A Number After a Double Reversal
 *
 * https://leetcode.com/problems/a-number-after-a-double-reversal/description/
 *
 * algorithms
 * Easy (79.07%)
 * Likes:    643
 * Dislikes: 37
 * Total Accepted:    77.7K
 * Total Submissions: 98.2K
 * Testcase Example:  '526'
 *
 * Reversing an integer means to reverse all its digits.
 *
 *
 * For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the
 * leading zeros are not retained.
 *
 *
 * Given an integer num, reverse num to get reversed1, then reverse reversed1
 * to get reversed2. Return true if reversed2 equals num. Otherwise return
 * false.
 *
 *
 * Example 1:
 *
 *
 * Input: num = 526
 * Output: true
 * Explanation: Reverse num to get 625, then reverse 625 to get 526, which
 * equals num.
 *
 *
 * Example 2:
 *
 *
 * Input: num = 1800
 * Output: false
 * Explanation: Reverse num to get 81, then reverse 81 to get 18, which does
 * not equal num.
 *
 *
 * Example 3:
 *
 *
 * Input: num = 0
 * Output: true
 * Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals
 * num.
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= num <= 10^6
 *
 *
 */

// @lc code=start
int reverse(int num)
{
    int rem, sum = 0, temp;
    temp = num;
    while (temp)
    {
        rem = temp % 10;
        sum = sum * 10 + rem;
        temp /= 10;
    }
    return sum;
}
bool isSameAfterReversals(int num)
{
    int temp1 = num;
    int temp2 = reverse(num);
    int temp3 = reverse(temp2);
    if (temp3 == temp1)
        return true;
    else
        return false;
}
// @lc code=end
