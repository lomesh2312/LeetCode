class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bot = -prices[0]
        ans = 0
        pre = 0
        for i in range(len(prices)):
            bot = max(bot, pre-prices[i])
            pre = max(pre, ans)
            ans = max(ans, bot + prices[i])
        return ans
        