class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        if len(favoriteCompanies)==1:
            return 0
        n = len(favoriteCompanies)
        arr_set = [set() for _ in xrange(n)]
        for i in xrange(n):
            arr_set[i] = set(favoriteCompanies[i])
        f = favoriteCompanies
        res = []
        for i in xrange(n):
            is_subset = False
            for j in xrange(n):
                if i==j:
                    continue
                if arr_set[i].issubset(arr_set[j]):
                    is_subset = True
                    break
            if not is_subset:
                res.append(i)
        return res