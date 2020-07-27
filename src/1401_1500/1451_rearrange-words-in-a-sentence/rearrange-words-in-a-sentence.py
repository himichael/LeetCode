class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        if not text:
            return text
        arr = text.split(" ")
        arr[0] = arr[0].lower()
        d = dict()
        n = len(arr)
        for i in xrange(n):
            i_len = len(arr[i])
            if i_len not in d:
                d[i_len] = [arr[i]]
            else:
                d[i_len].append(arr[i])
        res = []
        for key in sorted(d.keys()):
            res.extend(d[key])
        res[0] = res[0].title()
        return " ".join(res)