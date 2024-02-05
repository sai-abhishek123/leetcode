/*
 * @lc app=leetcode id=1492 lang=c
 *
 * [1492] The kth Factor of n
 *
 * https://leetcode.com/problems/the-kth-factor-of-n/description/
 *
 * algorithms
 * Medium (66.62%)
 * Likes:    1669
 * Dislikes: 287
 * Total Accepted:    194.4K
 * Total Submissions: 291.7K
 * Testcase Example:  '12\n3'
 *
 * You are given two positive integers n and k. A factor of an integer n is
 * defined as an integer i where n % i == 0.
 *
 * Consider a list of all factors of n sorted in ascending order, return the
 * k^th factor in this list or return -1 if n has less than k factors.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 12, k = 3
 * Output: 3
 * Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3^rd factor is 3.
 *
 *
 * Example 2:
 *
 *
 * Input: n = 7, k = 2
 * Output: 7
 * Explanation: Factors list is [1, 7], the 2^nd factor is 7.
 *
 *
 * Example 3:
 *
 *
 * Input: n = 4, k = 4
 * Output: -1
 * Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should
 * return -1.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= k <= n <= 1000
 *
 *
 *
 * Follow up:
 *
 * Could you solve this problem in less than O(n) complexity?
 *
 */

// @lc code=start
int kthFactor(int n, int k)
{
    int i, count = 0;
    for (i = 1; i <= n; i++)
    {
        if (n % i == 0)
            count++;
    }
    int *arr = (int *)malloc(count * sizeof(int));
    i = 0;
    for (int j = 1; j <= n; j++)
    {
        if (n % j == 0)
        {
            arr[i] = j;
            i++;
        }
    }
    if (k > count)
    {
        return -1;
    }
    else
    {
        return arr[k - 1];
    }
    free(arr);
}
// @lc code=end
