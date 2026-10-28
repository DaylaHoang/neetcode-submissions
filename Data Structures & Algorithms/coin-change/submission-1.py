class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[x] = minimum coins needed to make amount x.
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0 # Zero amount requires zero coins
        for target in range(1, amount + 1):
            for coin in coins:
                if coin <= target:
                    # Make the remaining amount first, then add 1 coin, keep whichever choice uses fewer coins
                    dp[target] = min(dp[target], dp[target - coin] + 1)
        # Inf means no combination can form the amount
        return -1 if dp[amount] == float("inf") else dp[amount]