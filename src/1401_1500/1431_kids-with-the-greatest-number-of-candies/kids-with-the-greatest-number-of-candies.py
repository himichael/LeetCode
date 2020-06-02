class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        ret = [candy + extraCandies >= maxCandies for candy in candies]
        return ret