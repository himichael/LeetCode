class Solution(object):
    def kClosest(self, points, K):
        points.sort(key=lambda x:(x[0] ** 2 + x[1] ** 2))
        return points[:K]