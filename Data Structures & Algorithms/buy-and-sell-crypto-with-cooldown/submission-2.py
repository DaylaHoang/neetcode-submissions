'''
1. Define 3 DP states:
    hold = max profit when holding a stock
    sold = max profit after selling today
    rest = max prodit without holding or selling today
2. Initalize the first day: hold, sold, rest
3. Process each remaining: new_hold, new_sold, new_rest
4. Return max(sold, rest)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        hold = -prices[0]
        sold = float("-inf")
        rest = 0
        for price in prices[1:]:
            new_hold = max(hold, rest - price)
            new_sold = hold + price
            new_rest = max(rest, sold)
            hold, sold, rest = new_hold, new_sold, new_rest
        return max(sold, rest)