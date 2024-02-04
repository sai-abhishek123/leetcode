/*
 * @lc app=leetcode id=3 lang=c
 *
 * [3] Longest Substring Without Repeating Characters
 *
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
 *
 * algorithms
 * Medium (34.43%)
 * Likes:    38607
 * Dislikes: 1790
 * Total Accepted:    5.4M
 * Total Submissions: 15.7M
 * Testcase Example:  '"abcabcbb"'
 *
 * Given a string s, find the length of the longest substring without repeating
 * characters.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "abcabcbb"
 * Output: 3
 * Explanation: The answer is "abc", with the length of 3.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "bbbbb"
 * Output: 1
 * Explanation: The answer is "b", with the length of 1.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "pwwkew"
 * Output: 3
 * Explanation: The answer is "wke", with the length of 3.
 * Notice that the answer must be a substring, "pwke" is a subsequence and not
 * a substring.
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= s.length <= 5 * 10^4
 * s consists of English letters, digits, symbols and spaces.
 *
 *
 */

// @lc code=start
int lengthOfLongestSubstring(char *s)
{

    int n = strlen(s);
    int max_length = 0;
    int start = 0;
    int end = 0;
    bool characters[128] = {false}; // Assume ASCII encoding

    while (end < n)
    {
        char c = s[end];
        if (!characters[c])
        {
            characters[c] = true;
            end++;
            max_length = fmax(max_length, end - start);
        }
        else
        {
            characters[s[start]] = false;
            start++;
        }
    }

    return max_length;
}
// @lc code=end
