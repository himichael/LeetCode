class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        n = len(words)
        res = []
        for i in xrange(n):
            for j in xrange(n):
                if i==j:
                    continue
                if words[j].find(words[i])>-1:
                    res.append(words[i])
                    break
        return res