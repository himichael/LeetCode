class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        s = set()
        d = dict()
        n = len(orders)
        for arr in orders:
            s.add(arr[2])
            i = int(arr[1])
            if i not in d:
                d[i] = dict()
                d[i][arr[2]] = 1
            else:
                if arr[2] in d[i]:
                    d[i][arr[2]] += 1
                else:
                    d[i][arr[2]] = 1
        res = []
        foods = sorted(s)
        first = ["Table"]
        for f in foods:
            first.append(f)
        res.append(first)
        for key in sorted(d.keys()):
            tmp = [str(key)]
            for f in foods:
                if f not in d[key]:
                    tmp.append("0")
                else:
                    tmp.append(str(d[key][f]))
            res.append(tmp)
        return res
        





