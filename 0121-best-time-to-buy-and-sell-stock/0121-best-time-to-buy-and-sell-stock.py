class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = prices[0]

        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                ans = max(ans,prices[i]-buy)
        return ans 