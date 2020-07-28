class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        d = dict()
        for arr in paths:
            d[arr[0]] = arr[1]
        for arr in paths:
            if arr[1] not in d:
                return arr[1]
        return ""    