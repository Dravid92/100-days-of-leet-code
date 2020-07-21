"""
Problem Statement
"""

"""

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5

"""

"""
Runtime: 44 ms, faster than 19.89% of Python3 online submissions for Length of Last Word.
Memory Usage: 13.9 MB, less than 38.90% of Python3 online submissions for Length of Last Word.
"""


"""
Solution
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        lst = s.split()
        
        if len(lst) >=1:
            fl = len(lst[-1])
        else:
            fl = 0
        
        return fl



