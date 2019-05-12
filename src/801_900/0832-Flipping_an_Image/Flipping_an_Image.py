class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in A:
            i.reverse()
            for x in range(len(i)):
                if i[x]==0:
                    i[x]=1
                else:
                    i[x]=0
        return A
        