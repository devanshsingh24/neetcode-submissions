class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrices=min(prices)
        n=prices.index(minPrices)
        m=prices[n:]
        maxPrices=max(m)
        return maxPrices - minPrices