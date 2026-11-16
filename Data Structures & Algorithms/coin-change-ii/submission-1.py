'''
1. Define a 1D DP array
    dp[a] = ways t o form amount a using processed denominations
2. Initalize base cases:
    dp = [0] * (amount + 1)
    dp[0] = 1
3. Process each coin, then each amount
4. Return dp[amount]
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]
        return dp[amount]