/*
 * @lc app=leetcode id=1979 lang=c
 *
 * [1979] Find Greatest Common Divisor of Array
 *
 * https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/
 *
 * algorithms
 * Easy (77.52%)
 * Likes:    1070
 * Dislikes: 45
 * Total Accepted:    116.6K
 * Total Submissions: 150.4K
 * Testcase Example:  '[2,5,6,9,10]'
 *
 * Given an integer array nums, return the greatest common divisor of the
 * smallest number and largest number in nums.
 *
 * The greatest common divisor of two numbers is the largest positive integer
 * that evenly divides both numbers.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [2,5,6,9,10]
 * Output: 2
 * Explanation:
 * The smallest number in nums is 2.
 * The largest number in nums is 10.
 * The greatest common divisor of 2 and 10 is 2.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [7,5,6,8,3]
 * Output: 1
 * Explanation:
 * The smallest number in nums is 3.
 * The largest number in nums is 8.
 * The greatest common divisor of 3 and 8 is 1.
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [3,3]
 * Output: 3
 * Explanation:
 * The smallest number in nums is 3.
 * The largest number in nums is 3.
 * The greatest common divisor of 3 and 3 is 3.
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= nums.length <= 1000
 * 1 <= nums[i] <= 1000
 *
 *
 */

// @lc code=start
int gcd_of_two_numbers(int a, int b)
{
    int gcd;
    for (int i = 1; i <= b; i++)
    {
        if (a % i == 0 && b % i == 0)
            gcd = i;
    }
    return gcd;
}
int findGCD(int *nums, int numsSize)
{
    int min, max, i;
    max = nums[0];
    min = max;
    for (i = 0; i < numsSize; i++)
    {
        if (nums[i] < min)
            min = nums[i];
        else if (nums[i] > max)
            max = nums[i];
    }
    return gcd_of_two_numbers(min, max);
}
// @lc code=end
