def maxProfit(prices):
        mini=prices[0]
        p=0
        n=len(prices)
        for i in range(n):
            cost = prices[i]-mini
            p=max(p,cost)
            mini=min(mini,prices[i])
        return p