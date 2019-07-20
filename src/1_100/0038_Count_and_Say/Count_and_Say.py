class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str    
        """
        #解析n-1的情况，然后拼接成一个字符串再递归调用n，最后返回
        def recursion(num,res):
            if(num == n):
                return res
            i,j = 0,1
            size = len(res)
            tmp = ""
            while(i < size):
                while(j<size and res[i]==res[j]):
                    j += 1
                x = j-i
                tmp = tmp + str(x) + res[i]
                i = j
            return recursion(num+1,tmp)
        return recursion(1,"1")