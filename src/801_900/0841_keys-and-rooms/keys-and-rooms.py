class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        visit = set()
        def dfs(index):
            visit.add(index)
            for i in rooms[index]:
                if 0<=i<n and i not in visit:
                    dfs(i)
        dfs(0)
        for i in xrange(0,n):
            if i not in visit:
                return False
        return True