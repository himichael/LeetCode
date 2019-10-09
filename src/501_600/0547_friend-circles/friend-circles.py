class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if( not M or len(M[0])==0 ):
            return 0
        n = len(M)
        self.queue = []
        self.count = 0
        def process():
            if( not self.queue ):
                return
            s = set(self.queue)
            while self.queue:
                index = self.queue.pop(0)
                for i in xrange(n):
                    if( M[index][i]==1 ):
                        M[index][i] = 0
                        if( i not in s ):
                            self.queue.append(i)
                            s.add(i)
            self.count += 1            
                
        for i in xrange(n):
            for j in xrange(n):
                if( M[i][j]==1 ):
                        M[i][j] = 0
                        self.queue.append(j)
            #process queue
            process()
        return self.count  