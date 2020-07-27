"""

121. Best Time to Buy and Sell Stock
Easy

5314

233

Add to List

Share
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lst=[]
        # i=0
        for i in range(len(prices)-1):
            # print(i)
            k = i+1
            for j in range(k,len(prices)):
                # print(j, len(prices)-1)
                if prices[j]>prices[i]:
                    n=prices[j]-prices[i]
                    lst.append(n)
                else:
                    pass
            # print(lst)
        if len(lst)==0:
            m = 0
        else:
            m = max(lst)

        return m

        
"""
Ran 199/200 test cases successfully, Last one time limit exceeded
"""