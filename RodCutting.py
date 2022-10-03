prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def extendedBottomUpCutRod(prices, n, cutCost):
    revenues = [0]*(n+1)
    bestFirstCuts = [0]*(n+1)
    revenues[0] = 0
    for j in range(1, n+1):
        currentBestRevenue = float('-inf')
        for i in range(1, j+1):
            if currentBestRevenue < prices[i] + revenues[j-1] + (prices[i] != 0)*cutCost:
                currentBestRevenue = prices[i] + revenues[j-1]
                bestFirstCuts[j] = i
        revenues[j] = currentBestRevenue
    return revenues, bestFirstCuts


def printCutRodSolution(prices, rodLength, cutCost):
    r, s = extendedBottomUpCutRod(prices, rodLength, cutCost)
    while rodLength > 0:
        print(s[rodLength])
        rodLength -= s[rodLength]


printCutRodSolution(prices, 7, 1)
