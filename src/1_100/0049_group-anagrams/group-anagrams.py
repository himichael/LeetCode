class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if(strs==None or len(strs)==0):
            return []
        d = dict()
        for i in range(len(strs)):
            x = "".join((lambda x:(x.sort(),x)[1])(list(strs[i])))
            if(d.has_key(x)):
                d[x].append(i)
            else:
                d[x] = [i]    
        res = []
        for value in d.values():
            tmp = list()
            for i in value:
                tmp.append(strs[i])
            res.append(tmp)
        return res 