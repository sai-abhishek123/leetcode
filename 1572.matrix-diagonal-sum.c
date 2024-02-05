/*
 * @lc app=leetcode id=1572 lang=c
 *
 * [1572] Matrix Diagonal Sum
 *
 * https://leetcode.com/problems/matrix-diagonal-sum/description/
 *
 * algorithms
 * Easy (82.77%)
 * Likes:    3375
 * Dislikes: 51
 * Total Accepted:    329.7K
 * Total Submissions: 398.3K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * Given a square matrix mat, return the sum of the matrix diagonals.
 *
 * Only include the sum of all the elements on the primary diagonal and all the
 * elements on the secondary diagonal that are not part of the primary
 * diagonal.
 *
 *
 * Example 1:
 *
 *
 * Input: mat = [[1,2,3],
 * [4,5,6],
 * [7,8,9]]
 * Output: 25
 * Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
 * Notice that element mat[1][1] = 5 is counted only once.
 *
 *
 * Example 2:
 *
 *
 * Input: mat = [[1,1,1,1],
 * [1,1,1,1],
 * [1,1,1,1],
 * [1,1,1,1]]
 * Output: 8
 *
 *
 * Example 3:
 *
 *
 * Input: mat = [[5]]
 * Output: 5
 *
 *
 *
 * Constraints:
 *
 *
 * n == mat.length == mat[i].length
 * 1 <= n <= 100
 * 1 <= mat[i][j] <= 100
 *
 *
 */

// @lc code=start
int diagonalSum(int **mat, int matSize, int *matColSize)
{
    int i, j, s1 = 0, s2 = 0, d1 = 0;
    for (i = 0; i < matSize; i++)
    {
        for (j = 0; j < matSize; j++)
        {
            if (i == j)
            {
                s1 += mat[i][j];
            }
        }
    }
    for (i = 0; i < matSize; i++)
    {
        for (j = matSize - 1; j >= 0; j--)
        {
            if (i + j == (matSize - 1))
            {
                s2 += mat[i][j];
            }
        }
    }
    if (matSize % 2 != 0)
    {
        d1 = mat[matSize / 2][matSize / 2];
    }
    return s2 + s1 - d1;
}
// @lc code=end
