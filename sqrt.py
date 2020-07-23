"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2

"""



class Solution:
    def mySqrt(self, x: int) -> int:
        
        s = x ** 0.5

        return int(s)


"""

Runtime: 32 ms, faster than 86.04% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.6 MB, less than 92.62% of Python3 online submissions for Sqrt(x).

"""