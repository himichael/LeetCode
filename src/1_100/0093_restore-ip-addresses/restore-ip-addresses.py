class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if(s==None or len(s)<4 or len(s)>12):
            return []
        res = []
        size = len(s)
        def recursion(level,index,arr):
            if(level==4):
                #print str(arr)+ "   index->"+str(index)+"  size->"+str(size)
                if(index == size):
                    tmp = ""
                    for i in arr:
                        tmp = tmp + "." + i
                    res.append( tmp[1:] )
                return
            for j in range(1,4):
                if(index+j > size):
                    break
                x = s[index:index+j]
                if(x.startswith("0") and len(x)>1):
                    continue
                if(int(x)>=0 and int(x)<=255):
                    recursion(level+1, index+j, arr+[x])
        recursion(0,0,[])
        return res