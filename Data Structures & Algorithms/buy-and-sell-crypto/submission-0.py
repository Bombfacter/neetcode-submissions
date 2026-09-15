class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        bestProfit = 0

        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                price = prices[right] - prices[left]
                bestProfit = max(bestProfit, price)

        return bestProfit