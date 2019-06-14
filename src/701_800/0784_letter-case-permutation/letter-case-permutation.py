class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        n = len(S)
        res = []
        def recursive(i,str):
            if(len(str) == n):
                res.append(str)
                return
            for j in range(i,len(S)):
                tmp = S[j]
                if(tmp.isalpha()):
                    for k in range(2):
                        if(tmp.islower()):
                            recursive(j+1,str+tmp.upper())
                            tmp = tmp.upper()
                        else:
                            recursive(j+1,str+tmp.lower())
                            tmp = tmp.lower()
                else:
                    recursive(j+1, str+tmp)       
                        
        recursive(0, "")
        return res