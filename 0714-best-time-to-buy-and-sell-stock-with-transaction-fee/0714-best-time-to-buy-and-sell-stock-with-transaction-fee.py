class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        bot = -prices[0]
        cash = 0

        for i in range(1, len(prices)):
            bot = max(bot, cash - prices[i])
            cash = max(cash, bot + prices[i] - fee)
        return cash
        